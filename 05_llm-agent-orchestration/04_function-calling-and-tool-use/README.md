# 04 Function Calling and Tool Use

이 단원은 LLM이 직접 답변만 생성하는 것이 아니라, 필요한 도구를 선택하고 Python 함수나 외부 API를 호출하는 구조를 학습합니다.

Agent를 만들 때 중요한 것은 “모델이 모든 것을 혼자 처리하게 하는 것”이 아니라, 모델은 판단하고 실제 작업은 Tool이 수행하도록 역할을 나누는 것입니다.

이 단원의 핵심 흐름은 다음입니다.

```text
사용자 요청
-> LLM이 필요한 Tool 판단
-> Python 함수 또는 외부 API 실행
-> Tool 결과를 다시 LLM에 전달
-> 최종 응답 생성
```

## 학습 목표

- Function Calling과 Tool Use의 차이를 이해합니다.
- Python 함수를 Tool로 설계하는 방법을 익힙니다.
- 외부 API 호출 결과를 Tool 결과로 다루는 흐름을 학습합니다.
- 여러 Tool 중 하나를 선택하는 Multi-Tool Router를 구현합니다.
- LangChain의 `@tool`과 `bind_tools` 흐름을 최소 수준으로 확인합니다.
- MCP 개념을 Function Calling과 비교하며 이해합니다.

## 폴더 구성

```text
04_function-calling-and-tool-use
├─ .env.example
├─ 00_references
│  └─ README.md
├─ 01_function-calling-basic
│  ├─ README.md
│  ├─ 01_simple-calculator-tool.py
│  └─ 02_learning-log-summary-tool.py
├─ 02_tool-use-with-external-api
│  ├─ README.md
│  ├─ 01_mock-weather-tool.py
│  └─ 02_http-api-tool-wrapper.py
├─ 03_multi-tool-orchestration
│  ├─ README.md
│  ├─ 01_multi-tool-router.py
│  └─ 02_manual-tool-selection-flow.py
├─ 04_langchain-tool-binding
│  ├─ README.md
│  ├─ 01_langchain_tool_decorator.py
│  └─ 02_bind_tools_basic.py
├─ 05_mcp-concept-and-optional-practice
│  ├─ README.md
│  ├─ 01_mcp-concept-summary.py
│  ├─ 02_simple_mcp_server.py
│  └─ 03_mcp_client_test.py
├─ 10_labs
└─ 20_assignments
```

## 실습 시작 순서

```powershell
cd C:\aidev\05_llm-agent-orchestration\04_function-calling-and-tool-use
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install openai python-dotenv httpx pydantic langchain-core langchain-openai
Copy-Item .env.example .env
```

이 단원의 `.env`는 `C:\aidev\05_llm-agent-orchestration\04_function-calling-and-tool-use\.env` 파일입니다.

## 실행 순서

```powershell
python .\01_function-calling-basic\01_simple-calculator-tool.py
python .\01_function-calling-basic\02_learning-log-summary-tool.py
python .\02_tool-use-with-external-api\01_mock-weather-tool.py
python .\02_tool-use-with-external-api\02_http-api-tool-wrapper.py
python .\03_multi-tool-orchestration\01_multi-tool-router.py
python .\03_multi-tool-orchestration\02_manual-tool-selection-flow.py
python .\04_langchain-tool-binding\01_langchain_tool_decorator.py
python .\04_langchain-tool-binding\02_bind_tools_basic.py
python .\05_mcp-concept-and-optional-practice\01_mcp-concept-summary.py
```

MCP 서버 예제는 선택 심화입니다. 진행하려면 `pip install mcp` 후 아래 명령을 실행합니다.

```powershell
python .\05_mcp-concept-and-optional-practice\03_mcp_client_test.py
```

## 단원별 핵심 연결

| 폴더 | 핵심 질문 |
| --- | --- |
| `01_function-calling-basic` | LLM이 Python 함수를 어떻게 선택하고 호출하는가? |
| `02_tool-use-with-external-api` | 외부 API 호출을 Tool로 감싸려면 무엇이 필요한가? |
| `03_multi-tool-orchestration` | 여러 Tool 중 어떤 Tool을 선택할지 어떻게 결정하는가? |
| `04_langchain-tool-binding` | LangChain Tool binding은 Function Calling과 어떻게 연결되는가? |
| `05_mcp-concept-and-optional-practice` | Function Calling과 MCP는 어떤 문제를 해결하려는가? |

## 수업 중 확인 질문

- LLM이 직접 답하는 경우와 Tool을 호출해야 하는 경우는 어떻게 구분하나요?
- Tool의 입력과 출력은 왜 명확히 설계해야 하나요?
- Multi-Tool Agent에서 Tool 선택 기준은 무엇인가요?
- LangChain Tool binding을 꼭 써야 하는 경우와 일반 Python Tool로 충분한 경우는 어떻게 구분하나요?
- MCP는 Function Calling과 어떤 문제의식에서 연결되나요?
