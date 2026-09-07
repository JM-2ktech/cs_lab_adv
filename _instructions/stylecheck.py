# -*- coding: utf-8 -*-
"""문체 검사 — 클로드 방언·번역투를 세어 점수로 낸다.

linkcheck.py 와 같은 자리에서 같은 방식으로 쓴다.
    python _instructions/stylecheck.py            전체
    python _instructions/stylecheck.py docs/lab6.md   지정

왜 만들었나 (2026-08-25)
    저작자가 생성하면서는 자기 리듬을 못 본다. 랩 본문에 「A가 아니라 B」가 57번,
    「~와 같습니다」류가 42번 쌓인 것을 세어 보고서야 알았다.
    CLAUDE.md 「쓰지 않는 것」 표에 있는 표현은 거의 안 나온다 — 표에 없던 것만 쌓였다.
    그래서 고칠 수 없는 생성 문제를 고칠 수 있는 검증 문제로 바꾼다.

세지 않는 것: frontmatter · 저작 메모(<!-- -->) · 코드블록 · 이미지 · 링크 주소 · IAL
"""
import io, os, re, sys, glob, json

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')  # cp949 콘솔에서 — 같은 글자가 깨지는 것을 막는다

# ── 규칙: (이름, 정규식, 1000자당 허용치, 가중치) ────────────────────
RULES = [
    # A. 대구 남발 — 이 저장소의 대표 버릇. 랩 간 연결을 한 문형으로만 처리했다
    ('대구: A가 아니라 B',      r'(?:가|이) 아니라 ',                        0.4, 4),
    ('대구: ~와 같다',          r'같습니다|같은 (?:얘기|구조|자리|종류|물건|그림)', 0.4, 4),
    ('대구: 여기서는/거기서는',  r'여기서는|거기서는',                          0.2, 4),
    # B. 번역투 — CLAUDE.md 「번역투 구문을 피한다」
    ('번역투: ~것입니다',        r'것입니다|것이다(?![\w가-힣])',              0.4, 3),
    ('번역투: ~뿐입니다',        r'뿐입니다',                                  0.2, 3),
    ('번역투: ~셈입니다',        r'셈입니다',                                  0.3, 2),
    ('번역투: ~라는 점',         r'라는 점',                                   0.2, 2),
    ('번역투: ~이 중요합니다',   r'(?:하는 것이|이) 중요합니다',                0.1, 2),
    # C. 강조를 부사로 — CLAUDE.md 「강조를 부사로 하지 않는다」
    ('부사 강조',               r'정말|사실은|놀랍게도|무엇보다|중요한 것은|핵심은', 0.2, 3),
    # D. 독자 심리 넘겨짚기 — CLAUDE.md
    ('심리 넘겨짚기',           r'당황하지|걱정하지|어렵지 않|잘못한 게|놓치기 쉽',  0.1, 4),
    # E. 진행 중계 — CLAUDE.md
    ('진행 중계',               r'아직 절반|거의 다 왔|여기까지 왔|이제 마지막',    0.1, 4),
    # F. 의인화 — CLAUDE.md 「사물을 의인화해 극적으로 만들지 않는다」
    ('의인화',                  r'끌려다니|새어나|알아서 처리하겠지',              0.2, 3),
    # G. 강조 지시 연발
    ('권유형 종결',             r'보세요|두세요|해 보세요',                      0.4, 2),
]
BOLD = re.compile(r'\*\*[^*\n]+\*\*')


def strip(md):
    """산문만 남긴다."""
    s = io.open(md, encoding='utf-8').read()
    s = re.sub(r'\A---\n.*?\n---\n', '', s, flags=re.S)   # frontmatter
    s = re.sub(r'<!--.*?-->', '', s, flags=re.S)          # 저작 메모
    s = re.sub(r'```.*?```', '', s, flags=re.S)           # 코드블록
    s = re.sub(r'^\s{4,}\S.*$', '', s, flags=re.M) if md.endswith('.nope') else s
    s = re.sub(r'!\[[^\]]*\]\([^)]*\)', '', s)            # 이미지
    s = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', s)        # 링크 → 표시문만
    s = re.sub(r'\{:[^}]*\}', '', s)                      # IAL
    s = re.sub(r'\[\^[\w-]+\]', '', s)                    # 각주 참조
    s = re.sub(r'`[^`\n]*`', '', s)                       # 인라인 코드
    s = re.sub(r'<[^>]+>', '', s)                         # 남은 HTML
    return s


FACT = [
    (r'\d[\d,\.]*',                  '숫자'),
    (r'`([^`\n]+)`',                  '인라인 코드'),
    (r'\]\(([^)]+)\)',                '링크·이미지 경로'),
    (r'\[\^[\w-]+\]',                '각주'),
    (r'\{:[^}]*\}',                   'IAL'),
    (r'[A-Za-z][A-Za-z0-9_\-\.]{3,}', '영문 식별자'),
]


def facts(md):
    """윤색이 건드리면 안 되는 것들. 어투를 고쳐도 이 집합은 그대로여야 한다."""
    s = re.sub(r'<!--.*?-->', '', io.open(md, encoding='utf-8').read(), flags=re.S)
    out = set()
    for pat, _ in FACT:
        out |= set(m if isinstance(m, str) else m[0] for m in re.findall(pat, s))
    return out


def fact_cmd(argv):
    """--facts save <파일>  /  --facts diff <파일>"""
    mode, md = argv[0], argv[1]
    store = '_instructions/.facts.json'
    if mode == 'save':
        json.dump({md: sorted(facts(md))}, io.open(store, 'w', encoding='utf-8'), ensure_ascii=False)
        print('사실 토큰 %d개 저장 — %s' % (len(facts(md)), md))
        return 0
    before = set(json.load(io.open(store, encoding='utf-8')).get(md, []))
    after = facts(md)
    lost, new = sorted(before - after), sorted(after - before)
    if not lost and not new:
        print('PASS  사실 변경 0건 (%d개 대조)' % len(after))
        return 0
    print('FAIL  사실이 바뀌었다')
    if lost:
        print('  사라짐 %d: %s' % (len(lost), ', '.join(lost[:12])))
    if new:
        print('  생김   %d: %s' % (len(new), ', '.join(new[:12])))
    return 1


def bold_density(s):
    """문단당 볼드 2개 이상인 문단의 비율. CLAUDE.md 「한 문단에 볼드는 하나까지」."""
    paras = [p for p in re.split(r'\n\s*\n', s) if len(p.strip()) > 40]
    if not paras:
        return 0.0, 0, 0
    over = [p for p in paras if len(BOLD.findall(p)) >= 2]
    return len(over) / len(paras), len(over), len(paras)


def score(md):
    s = strip(md)
    n = max(len(re.sub(r'\s', '', s)), 1)
    k = n / 1000.0
    rows, penalty = [], 0.0
    for name, pat, allow, weight in RULES:
        c = len(re.findall(pat, s))
        d = c / k
        over = max(0.0, d - allow)
        p = over * weight
        penalty += p
        if c:
            rows.append((name, c, d, allow, p))
    ratio, over_n, para_n = bold_density(s)
    bp = max(0.0, ratio - 0.12) * 70      # CLAUDE.md는 문단당 볼드 하나. 12%까지만 봐준다
    penalty += bp
    return max(0, round(100 - penalty)), rows, (ratio, over_n, para_n, bp), n


def grade(v):
    return 'A' if v >= 90 else 'B' if v >= 75 else 'C' if v >= 60 else 'D'


def main(targets):
    if not targets:
        targets = (sorted(glob.glob('docs/*.md')) + sorted(glob.glob('docs/appendix/*.md'))
                   + sorted(glob.glob('_instructions/decks/*-intermission.md')) + ['index.md', 'README.md'])
    targets = [t for t in targets if os.path.exists(t)]
    print('%-34s %6s %5s %7s  %s' % ('파일', '점수', '등급', '글자', '가장 큰 감점'))
    print('-' * 92)
    worst, results = [], []
    for md in targets:
        v, rows, bold, n = score(md)
        cand = list(rows) + ([('볼드 과다', bold[1], 0, 0, bold[3])] if bold[3] > 0 else [])
        cand.sort(key=lambda r: -r[4])
        top = ('%s ×%d  -%.0f' % (cand[0][0], cand[0][1], cand[0][4])) if cand and cand[0][4] > 0.5 else '-'
        print('%-34s %6d %5s %7d  %s' % (md.replace(os.sep, '/'), v, grade(v), n, top))
        results.append((md, v, rows, bold))
        if v < 75:
            worst.append((md, v, rows, bold))
    print()
    if worst:
        print('■ 75점 미만 상세')
        for md, v, rows, bold in worst:
            print('  %s  (%d점)' % (md.replace(os.sep, '/'), v))
            for name, c, d, allow, p in rows:
                if p > 0.3:
                    print('     %-24s %3d회  %.1f/1000자 (허용 %.1f)  -%.0f' % (name, c, d, allow, p))
            if bold[3] > 0.3:
                print('     %-24s %3d/%d 문단이 볼드 2개 이상  -%.0f' % ('볼드 과다', bold[1], bold[2], bold[3]))
            print()
    avg = sum(r[1] for r in results) / len(results)
    print('평균 %.1f점 · A %d · B %d · C %d · D %d' % (
        avg, *[sum(1 for r in results if grade(r[1]) == g) for g in 'ABCD']))
    # 감점이 어디서 나오는지 — 고칠 순서를 정하는 자리
    agg, boldp = {}, 0.0
    for _, _, rows, bold in results:
        boldp += bold[3]
        for name, c, d, allow, pen in rows:
            if pen > 0:
                agg[name] = agg.get(name, 0) + pen
    total = boldp + sum(agg.values())
    if total:
        print()
        print('■ 감점 구성 (전체 %.0f점)' % total)
        print('   %-24s %6.0f  %4.0f%%' % ('볼드 과다', boldp, 100 * boldp / total))
        for name, pen in sorted(agg.items(), key=lambda x: -x[1])[:6]:
            print('   %-24s %6.0f  %4.0f%%' % (name, pen, 100 * pen / total))
    return 1 if avg < 75 else 0


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    if len(sys.argv) > 3 and sys.argv[1] == '--facts':
        sys.exit(fact_cmd(sys.argv[2:]))
    sys.exit(main(sys.argv[1:]))
