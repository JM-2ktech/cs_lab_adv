# cs_lab_adv — Copilot Studio 중급 교안

HR 채용 자동화를 소재로 커넥터·에이전트 흐름·승인·토픽을 다루는 **2일차(중급) 과정**입니다.
랩 7개 + 부록 3종, 220분.

입문 과정은 별도 저장소입니다 — [cs_lab](https://jm-2ktech.github.io/cs_lab/).

## 로컬 실행

```bash
bundle install
bundle exec jekyll serve
```

## 검증

```bash
bundle exec jekyll build
python _instructions/linkcheck.py
python _instructions/stylecheck.py
python ../_tools/sync_infra.py    # 공유 인프라가 cs_lab 과 어긋나지 않았는지 (이 저장소만 클론했다면 건너뜁니다)
```

`linkcheck.py` 는 `ADVANCED`·`OTHER`·`step numbering` 이 셋 다 0 이어야 통과합니다.

## 작업 중인 것

스크린샷 재촬영과 본문 교정을 진행 중입니다.

- [_instructions/실측_리포트_2026-09.md](_instructions/실측_리포트_2026-09.md) — **무엇을** 고쳐야 하는가
- [_instructions/작업_지침.md](_instructions/작업_지침.md) — **어떻게** 고치는가

## 실습 환경

본문의 SharePoint 사이트는 `https://2ktech.sharepoint.com/sites/edulab` (표시명 **에듀랩**)입니다.
다른 테넌트에서 진행하려면 이 두 문자열을 먼저 치환합니다.

시나리오(HR 채용, 지원자 목록)와 스크린샷은 이 환경 기준입니다.
