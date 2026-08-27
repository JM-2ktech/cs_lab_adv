# cs_lab_adv — Copilot Studio 중급 교안

HR 채용 자동화를 소재로 커넥터·에이전트 흐름·승인·토픽을 다루는 **2일차(중급) 과정**입니다.
랩 7개 + 부록 3종, 230분.

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
```

## ⚠️ 배포하지 않습니다

본문에 고객사명이 남아 있습니다(9개 파일 27행). **탈CJ 이전에는 공개 대상이 아닙니다.**
`_config.yml` 의 `url` 이 비어 있는 것이 그 이유입니다.
