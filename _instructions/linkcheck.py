import io, os, re, sys, glob, urllib.parse

root = '_site'

# baseurl 은 _config.yml 에서 읽는다. 교안 저장소가 셋(cs_lab · cs_lab_adv · cs_lab_ghcp)이고
# 이 파일은 세 곳에 복사돼 돌아간다. 하드코딩하면 사본마다 갈라지고, 갈라진 것은 조용히 낡는다.
baseurl = ''
if os.path.exists('_config.yml'):
    for line in io.open('_config.yml', encoding='utf-8'):
        m = re.match(r'^baseurl:\s*"?([^"]*?)"?\s*$', line)
        if m:
            baseurl = m.group(1).strip().rstrip('/')
            break
prefix = (baseurl + '/') if baseurl else '/'
bad = []
for dp, _, fns in os.walk(root):
    for fn in fns:
        if not fn.endswith('.html'):
            continue
        f = os.path.join(dp, fn)
        s = open(f, encoding='utf-8', errors='ignore').read()
        for u in re.findall(r'(?:href|src)="([^"]+)"', s):
            if u.startswith(('http', '#', 'mailto', 'data:', 'javascript')):
                continue
            p = urllib.parse.unquote(u.split('#')[0])
            if not p:
                continue
            if p.startswith(prefix):
                t = os.path.join(root, p[len(prefix):])
            else:
                t = os.path.join(dp, p)
            if not (os.path.exists(t) or os.path.exists(os.path.join(t, 'index.html'))):
                bad.append((os.path.relpath(f, root).replace(os.sep, '/'), u))

# labN-NN.png = 랩 스텝 컷, appendix/<슬러그>-NN.png = 부록 컷. 둘 다 미촬영 예정분으로 센다.
placeholder = [b for b in bad if re.search(r'assets/lab\d/lab\d-\d\d[b-z]?\.png$|assets/appendix/[a-z-]+-\d\d[b-z]?\.png$', b[1])]
advanced = [b for b in bad if 'advanced' in b[0] or 'advanced' in b[1]]
other = [b for b in bad if b not in placeholder and b not in advanced]

print('total broken                        : %d' % len(bad))
print('  beginner placeholder screenshots  : %d  (expected, not yet shot)' % len(placeholder))
print('  ADVANCED  (must be 0)             : %d' % len(advanced))
for f, u in advanced[:20]:
    print('     %s -> %s' % (f, u))
print('  OTHER     (must be 0)             : %d' % len(other))
for f, u in other[:20]:
    print('     %s -> %s' % (f, u))
# ── 스텝 번호 이어지기 ──────────────────────────────────────────────
# 테마가 CSS 카운터로 번호를 그려서 HTML의 start 속성을 무시한다.
# custom.scss가 ol[start] 를 되살리므로 마크다운 쪽 {: start="N" } 만 맞으면 되는데,
# 이 IAL은 `---` 뒤에 오거나 앞에 빈 줄이 있으면 조용히 무효가 된다(2회 재발).
# 마크다운에서 "이 절은 N번부터"를 읽어 내고, 렌더된 HTML에 그 start가 살아 있는지 본다.
numbad = []
for md in sorted(glob.glob('docs/**/*.md', recursive=True)):
    body = re.sub(r'<!--.*?-->', '', open(md, encoding='utf-8').read(), flags=re.S)
    want = set()
    # ## 뿐 아니라 ### 도 목록을 끊는다. docs/appendix/connected-agent.md 가
    # ### 소제목 두 개로 목록을 끊는데 ## 만 보다가 놓쳤다(2026-08-20).
    for chunk in re.split(r'^#{2,3} ', body, flags=re.M)[1:]:
        m = re.search(r'^(\d+)\. ', chunk, re.M)
        if m and m.group(1) != '1':
            want.add(int(m.group(1)))
    if not want:
        continue
    html = os.path.join(root, os.path.splitext(md)[0].replace(os.sep, '/') + '.html')
    if not os.path.exists(html):
        continue
    got = set(int(x) for x in re.findall(r'<ol start="(\d+)"', open(html, encoding='utf-8').read()))
    for n in sorted(want - got):
        numbad.append((md.replace(os.sep, '/'), n))

print('  step numbering (must be 0)          : %d' % len(numbad))
for f, n in numbad[:20]:
    print('     %s : %d번부터인 절의 start IAL이 렌더에 없음' % (f, n))

sys.exit(1 if (advanced or other or numbad) else 0)
