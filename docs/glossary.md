---
title: 중급 부록. 용어집
nav_order: 12
---

# 부록. 용어집 📚

이 과정에 등장하는 약어와 핵심 용어를 모았습니다. 본문을 읽다가 낯선 말이 나오면 이 페이지를 참고하세요.

## 약어

| 약어 | 풀네임 | 한 줄 설명 |
|---|---|---|
| <span id="abbr-sp">**SP**</span> | [SharePoint](https://learn.microsoft.com/sharepoint/introduction) | Microsoft 365의 협업·데이터 플랫폼. 이 과정에서 지원자 목록과 이력서 파일의 저장소로 사용한다 |
| <span id="abbr-hitl">**HITL**</span> | [Human-in-the-Loop](https://learn.microsoft.com/power-automate/get-started-approvals) | AI 자동화 중간에 **사람의 검토·승인·결정**을 끼워 넣는 설계 패턴. 이 과정의 핵심 주제 |
| <span id="abbr-pad">**PAD**</span> | [Power Automate Desktop](https://learn.microsoft.com/power-automate/desktop-flows/introduction) | PC 화면을 직접 조작하는 데스크톱 자동화(RPA) 도구. 오프닝 시연에 등장 |
| <span id="abbr-cs">**CS**</span> | [Copilot Studio](https://learn.microsoft.com/microsoft-copilot-studio/fundamentals-what-is-copilot-studio) | Microsoft의 에이전트(챗봇) 제작 플랫폼. 이 과정의 주 무대 |
| <span id="abbr-rag">**RAG**</span> | [Retrieval-Augmented Generation](https://learn.microsoft.com/microsoft-copilot-studio/guidance/retrieval-augmented-generation) | 검색 증강 생성 — 질문과 관련된 문서 조각을 찾아 AI 답변의 근거로 사용하는 기술. Knowledge가 이 방식으로 동작한다 |
| <span id="abbr-jd">**JD**</span> | Job Description | 직무기술서 — 직군별 필수·우대 요건을 정의한 문서. Knowledge 4종 중 하나 |
| <span id="abbr-mcp">**MCP**</span> | Model Context Protocol | AI 에이전트가 외부 도구·데이터 소스에 연결하기 위한 오픈 표준 프로토콜(Anthropic 제안, 업계 채택). 부록의 MS Learn 도구 연결이 이 방식으로 동작한다 |
| <span id="abbr-a2a">**A2A**</span> | Agent-to-Agent | 에이전트 간 통신을 위한 오픈 표준 프로토콜. 한 에이전트가 다른 에이전트에 작업을 위임하고 결과를 받는 구조를 정의한다. Copilot Studio는 같은 환경의 CS 에이전트 연결과 외부 A2A 에이전트 연결 모두를 지원한다. 부록의 자가진단 에이전트가 이 패턴의 실습 예시다 |

## 핵심 개념

| 용어 | 설명 |
|---|---|
| <span id="term-list">**목록 (List)**</span> | 행·열로 구성된 SharePoint 데이터 저장소. 지원자 한 명이 한 행(항목), 이름·이메일·전형단계 등 속성이 각 컬럼에 해당한다. 이 과정에서 모든 지원자 정보가 집결하는 **단일 진실 원천(Single Source of Truth)** 으로, 흐름과 에이전트가 공통으로 읽고 쓰는 중심 데이터다 (Lab 1) → [Microsoft 365 목록 소개](https://support.microsoft.com/office/introduction-to-lists-0a1c3ace-def0-44af-b225-cfa8d92c52d7) |
| <span id="term-internal-name">**내부 이름 (Internal Name)**</span> | 컬럼을 처음 만들 때 부여되는 시스템 식별자. 이후 표시 이름을 변경해도 내부 이름은 고정된다. 흐름의 동적 콘텐츠 참조나 OData 필터 쿼리가 이 이름을 사용하므로, 영문으로 생성하는 것이 권장된다 (Lab 1) |
| <span id="term-flow">**흐름 (Flow)**</span> | 트리거 → 액션 순서로 실행되는 자동화 단위. 같은 입력에 항상 같은 동작을 하는 **결정적(deterministic) 실행**이 특징이며, 상태 변경·이벤트 처리처럼 일관성이 중요한 작업에 적합하다. 이 과정에서는 적재 흐름(Lab 4)·승인 흐름(Lab 5)·AI 적합도 반영 흐름(Lab 6)·전형단계 변경 흐름(Lab 7)이 해당된다 → [MS Learn: 에이전트 흐름 개요](https://learn.microsoft.com/microsoft-copilot-studio/flows-overview) |
| <span id="term-connector">**커넥터 (Connector)**</span> | 에이전트나 흐름이 외부 시스템(SharePoint, Outlook 등)에 접근하는 연결 통로. 에이전트의 도구 탭에서 커넥터를 도구로 등록하면, 오케스트레이터가 사용자 질의에 따라 해당 커넥터를 자동으로 호출하고 결과를 답변 근거로 활용한다 → [MS Learn: 커넥터 개요](https://learn.microsoft.com/connectors/overview) |
| <span id="term-tool">**도구 (Tool)**</span> | Copilot Studio 에이전트에 등록하는 외부 기능 연결 단위. 커넥터·MCP 서버·흐름 등을 도구로 추가하면, 오케스트레이터가 사용자 발화에 따라 적절한 도구를 자동으로 선택·호출하고 결과를 답변 근거로 사용한다. **도구 설명(description)이 라우팅의 핵심** — 오케스트레이터는 이 설명을 보고 어떤 도구를 언제 부를지 결정한다 (Lab 3) → [MS Learn: Copilot Studio 도구(액션)](https://learn.microsoft.com/microsoft-copilot-studio/advanced-plugin-actions) |
| <span id="term-agent">**에이전트 (Agent)**</span> | Copilot Studio로 구성하는 AI 대화 인터페이스. 사용자의 발화를 해석해 적절한 지식을 참조하거나 도구를 호출하고, 그 결과를 자연어 답변으로 생성한다. 지식·도구·지침을 조합해 동작하며, 이 과정의 중심 산출물이다 → [MS Learn: 에이전트란?](https://learn.microsoft.com/microsoft-copilot-studio/fundamentals-what-is-copilot-studio#what-is-an-agent) |
| <span id="term-knowledge">**지식 (Knowledge)**</span> | 에이전트에 등록하는 참조 문서. 에이전트가 답변을 생성할 때 근거로 삼는 **"기준"** 을 담는다. 이 과정에서는 채용 가이드·직무기술서(JD)·회사 지침·평가 루브릭 4종을 사용한다. 실시간으로 변경되는 지원자 데이터(목록)와 이력서 원문(파일)은 Knowledge가 아니라 커넥터와 링크로 접근한다 (Lab 2) → [MS Learn: RAG in Copilot Studio](https://learn.microsoft.com/microsoft-copilot-studio/guidance/retrieval-augmented-generation) |
| <span id="term-corpus">**코퍼스 (Corpus)**</span> | RAG 검색 대상이 되는 문서 전체 집합. 에이전트는 질문과 관련된 조각을 이 집합 전체에서 검색한다. 이력서 수백 개를 한 코퍼스에 등록하면 "특정 지원자 한 명"만 명확하게 분리하기 어렵고 다른 지원자 내용이 혼입될 수 있다 — 이것이 이력서를 Knowledge에 등록하지 않고 링크로 1건씩 가져오는 이유다 (Lab 2·3) |
| <span id="term-instructions">**지침 (Instructions)**</span> | 에이전트의 행동 규칙을 자연어로 작성한 텍스트. 시스템 프롬프트에 해당하며, 어떤 도구를 언제 사용할지·어떤 데이터를 표시할지·무엇을 답하지 않을지 등 에이전트의 전반적인 행동 양식을 결정한다. 흐름이 코드로 분기를 정의하는 것과 달리, 지침은 자연어로 의도를 전달해 에이전트가 상황에 맞게 해석한다 → [MS Learn: 에이전트 지침 설정](https://learn.microsoft.com/microsoft-copilot-studio/nlu-generative-answers-prompt-modification) |
| <span id="term-markdown">**MD**, **Markdown**</span> | 특수 기호로 서식을 지정하는 경량 마크업 언어. `**굵게**`, `## 제목`, `- 목록` 처럼 사람이 읽기 쉬운 텍스트로 구조를 표현한다. Copilot Studio 지침은 Markdown으로 작성하며, `##` 헤더로 섹션을 나누고 `-` 목록으로 규칙을 열거하면 에이전트가 지침을 더 일관성 있게 따른다. → [Markdown 기본 문법](https://www.markdownguide.org/basic-syntax/) |
| <span id="term-guardrail">**가드레일 (Guardrail)**</span> | 지침으로 에이전트의 행동 범위를 좁히는 제약. "이 도구만 사용한다", "승인된 지원자만 표시한다", "데이터에 없는 내용은 생성하지 않는다"처럼, 에이전트가 의도를 벗어난 답변을 생성하는 것을 방지한다. 줄일 수 있는 모호함을 줄여 오답이 발생할 수 있는 범위 자체를 좁히는 것이 목적이다 (Lab 3·6) |
| <span id="term-topic">**토픽 (Topic)**</span> | Copilot Studio 에이전트 안에서 특정 주제·요청을 처리하는 단위 시나리오. 특정 발화 패턴이 인식되면 해당 토픽이 활성화되어 메시지·질문·조건·액션 호출 등 설정된 노드를 순서대로 실행한다. 이 과정에서는 전형단계 변경 흐름을 호출하며 게이트·확인 카드로 사람 확인(대화형 HITL)을 끼워 넣는 토픽이 대표 예시다 (Lab 7) → [MS Learn: 토픽 만들기·편집](https://learn.microsoft.com/microsoft-copilot-studio/authoring-create-edit-topics) |
| <span id="term-content-approval">**콘텐츠 승인 / 승인상태**</span> | SharePoint 내장 기능. 목록 항목을 승인됨·거부됨·보류 중으로 관리한다. 직접 생성하는 컬럼이 아니라 SharePoint가 제공하는 내장 컬럼(`OData__ModerationStatus`)이며, 커넥터의 일반 항목 업데이트로는 변경할 수 없다. Lab 1에서 목록·문서 라이브러리 설정 시 활성화하는 기능이다 (Lab 1) |
| <span id="term-summary-approval-status">**요약승인상태**</span> | 승인 흐름이 결과를 기록하는 **직접 생성한 Choice 컬럼**. 값은 승인대기(기본)·승인됨·거부됨 세 가지. Approvals 커넥터의 결과(Approve → `승인됨` / Reject → `거부됨`)에 따라 승인 흐름이 이 값을 갱신한다. SP 내장 콘텐츠 승인(`OData__ModerationStatus`)과 완전히 별개이며, Lab 3의 "승인된 지원자만 조회" 지침이 이 컬럼 값을 기준으로 동작한다 (Lab 1·5) |
| <span id="term-review-status">**전형단계**</span> | 채용 진행 단계를 기록하는 직접 생성한 Choice 컬럼(내부명 ReviewStatus). **검토중(기본값)·서류합격·불합격 세 가지 값**을 가진다. SharePoint 내장 승인상태와는 완전히 별개의 컬럼으로, 전형단계 변경(Lab 7 토픽)이 이 값을 변경한다. "면접합격"·"최종합격"은 이 컬럼에 없는 값이며, Lab 7의 오케스트레이터 지침이 그런 요청을 차단한다 (Lab 1·7) |
| <span id="term-transaction">**트랜잭션**</span> | 여러 데이터 변경이 "전부 성공 또는 전부 취소"로 묶여야 하는 작업 단위. 이 과정에서는 AI 적합도 반영(Lab 6)과 전형단계 변경(Lab 7)이 해당된다 — 조회·검증·갱신이 한 덩어리로 묶여야 하고, 검증에 실패하면 갱신이 아예 일어나면 안 된다. 확률적으로 동작하는 에이전트가 아닌 결정적 흐름이 담당해야 하는 핵심 근거다 (Lab 6·7) |
| <span id="term-rubric">**평가 루브릭**</span> | 지원자 적합도를 등급으로 환산하는 채점 규칙 문서. 5개 축(R1 직군 요건·R2 경력 레벨·R3 성과·R4 협업·R5 인재상)으로 구성되며, 에이전트의 적합도 평가(C2)가 이 루브릭을 Knowledge로 참조해 등급을 산출한다. Knowledge 4종의 키스톤 역할을 한다 (Lab 2·3) |
| <span id="term-citizen-dev">**시티즌 개발자**</span> | 전문 프로그래머가 아니지만 로우코드·노코드 도구를 활용해 업무 자동화를 직접 구현하는 현업 담당자. 이 과정의 주 대상이다 → [MS Learn: 융합 개발과 시티즌 개발자](https://learn.microsoft.com/power-platform/developer/fusion-development) |
| <span id="term-ai-builder">**AI Builder**</span> | Power Automate 안에서 제공하는 AI 기능 모음. 이 과정에서는 적재 흐름의 이력서 텍스트 추출·구조화에 사용한다 (Lab 4) → [MS Learn: AI Builder 개요](https://learn.microsoft.com/ai-builder/overview) |
| <span id="term-json">**JSON**</span> | JSON(JavaScript Object Notation)은 시스템 간에 데이터를 주고받기 위해 사용하는 경량 데이터 형식입니다. 사람이 읽기 쉽고 컴퓨터가 처리하기 쉬워 Copilot Studio, Power Automate, API 연동 등에서 널리 사용됩니다. JSON은 `Key: Value` 구조를 기본으로 하며, 객체(`{}`)와 배열(`[]`)을 조합해 다양한 데이터를 표현합니다. [json.org](https://www.json.org/json-ko.html)|
| <span id="term-mcp">**MCP (Model Context Protocol)**</span> | AI 에이전트가 외부 도구·데이터 소스에 표준 방식으로 연결하기 위한 오픈 프로토콜. 에이전트는 MCP 서버 URL 하나만 등록하면 그 서버가 제공하는 도구 전체를 쓸 수 있다. 부록에서 `https://learn.microsoft.com/api/mcp`를 등록하는 것만으로 MS Learn 문서 검색 기능 전체가 자가진단 에이전트의 도구가 되는 것이 그 예시다. Copilot Studio는 MCP 서버 연결을 공식 지원하며, 별도 커넥터 개발 없이 외부 기능을 빠르게 붙일 수 있다는 점이 장점이다. [Agent Extend Action MCP](https://learn.microsoft.com/microsoft-copilot-studio/agent-extend-action-mcp) |
| <span id="term-a2a">**연결된 에이전트 / A2A (Agent-to-Agent)**</span> | 한 에이전트(오케스트레이터)가 다른 에이전트를 하위 에이전트로 등록하고, 사용자 요청에 따라 작업을 위임하는 패턴. Copilot Studio에서는 같은 환경의 CS 에이전트를 "연결된 에이전트"로 추가하거나, 외부에서 A2A 프로토콜로 구현된 에이전트를 연결할 수 있다. 부록의 자가진단 에이전트 → 면접관 에이전트 구조가 전자(CS 내부 연결)의 실습 예시다. 요청을 받은 오케스트레이터가 어떤 하위 에이전트를 호출할지를 **하위 에이전트의 설명(description)** 을 보고 자동으로 결정하므로, 설명을 명확하게 쓰는 것이 라우팅 정확도의 핵심이다. → [MS Learn: Add other agents overview](https://learn.microsoft.com/microsoft-copilot-studio/authoring-add-other-agents) |

