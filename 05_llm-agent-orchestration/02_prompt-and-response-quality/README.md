# 02 Advanced Prompting and Reasoning

이 단원은 프롬프트를 더 안정적으로 설계하는 방법을 학습합니다. 단순히 질문을 던지는 수준을 넘어 역할, 지시문, 맥락, 출력 형식을 명확히 나누어 LLM 응답 품질을 개선합니다.

01 단원에서 LLM을 호출하는 방법을 배웠다면, 02 단원에서는 “어떻게 요청해야 더 안정적인 응답을 얻을 수 있는가”를 다룹니다.

핵심 흐름은 다음과 같습니다.

```text
단순 질문
-> 역할, 지시문, 맥락 분리
-> 원하는 출력 형식 지정
-> JSON/Pydantic으로 응답 구조 검증
-> 위험 입력 방어
-> 프롬프트 버전별 품질 비교
```

## 학습 목표

- Role, Instruction, Context 구조로 프롬프트를 작성합니다.
- Few-shot 예시를 사용해 원하는 답변 스타일을 유도합니다.
- JSON 형식 응답과 Pydantic 기반 Structured Output을 이해합니다.
- Plan-Act-Review, ReAct 스타일 사고 흐름을 코드로 살펴봅니다.
- Prompt Injection을 이해하고 입력 검증과 안전한 시스템 지시문을 적용합니다.

## 폴더 구성

```text
02_prompt-and-response-quality
├─ .env.example
├─ 00_references
│  └─ README.md
├─ 01_prompt-design-patterns
│  ├─ README.md
│  ├─ 01_role-and-context-prompt.py
│  └─ 02_few-shot-style-prompt.py
├─ 02_structured-output-json
│  ├─ README.md
│  ├─ 01_json-output-request.py
│  └─ 02_structured-output-pydantic.py
├─ 03_reasoning-and-react-basics
│  ├─ README.md
│  ├─ 01_plan-act-review-pattern.py
│  └─ 02_react-style-without-tools.py
├─ 04_prompt-safety-and-evaluation
│  ├─ README.md
│  ├─ 01_prompt-injection-defense.py
│  └─ 02_prompt-version-evaluation.py
├─ 10_labs
└─ 20_assignments
```

## 실습 시작 순서

```powershell
cd C:\aidev\05_llm-agent-orchestration\02_prompt-and-response-quality
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install openai python-dotenv pydantic
Copy-Item .env.example .env
```

이 단원의 `.env`는 `C:\aidev\05_llm-agent-orchestration\02_prompt-and-response-quality\.env` 파일입니다. 01 단원의 `.env`를 자동으로 읽지 않으므로, 이 단원에서도 `.env.example`을 `.env`로 복사해야 합니다.

OpenAI API Key가 없으면 예제는 실제 호출을 하지 않고 안전하게 종료됩니다. 이 단원은 OpenAI 응답을 바탕으로 프롬프트 품질을 비교하므로, 가능하면 API Key를 준비한 뒤 진행하는 것이 좋습니다.

## 실행 순서

```powershell
python .\01_prompt-design-patterns\01_role-and-context-prompt.py
python .\01_prompt-design-patterns\02_few-shot-style-prompt.py
python .\02_structured-output-json\01_json-output-request.py
python .\02_structured-output-json\02_structured-output-pydantic.py
python .\03_reasoning-and-react-basics\01_plan-act-review-pattern.py
python .\03_reasoning-and-react-basics\02_react-style-without-tools.py
python .\04_prompt-safety-and-evaluation\01_prompt-injection-defense.py
python .\04_prompt-safety-and-evaluation\02_prompt-version-evaluation.py
```

## 단원별 핵심 연결

| 폴더 | 핵심 질문 |
| --- | --- |
| `01_prompt-design-patterns` | 역할, 지시문, 맥락을 나누면 응답이 어떻게 달라지는가? |
| `02_structured-output-json` | LLM 응답을 프로그램에서 바로 쓰려면 어떤 구조가 필요한가? |
| `03_reasoning-and-react-basics` | 도구를 쓰기 전에 어떤 순서로 판단하게 만들 것인가? |
| `04_prompt-safety-and-evaluation` | 사용자의 위험한 입력을 어떻게 구분하고 방어할 것인가? |

## 수업 중 확인 질문

- Role, Instruction, Context를 나누면 어떤 점이 좋아지나요?
- JSON 응답을 요청하는 것과 Pydantic으로 검증하는 것은 어떤 차이가 있나요?
- ReAct 구조에서 Reasoning과 Action은 각각 어떤 역할을 하나요?
- Prompt Injection은 왜 위험하고, 어떤 방식으로 방어할 수 있나요?
- 프롬프트 개선 전후를 비교할 때 어떤 기준으로 평가해야 하나요?
