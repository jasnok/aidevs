# 04_langchain-tool-binding

이 챕터에서는 LangChain에서 Python 함수를 Tool로 등록하고 LLM에 연결하는 기본 흐름을 확인합니다.

05 과정에서 LangChain은 깊게 다루지 않습니다. 여기서는 LangGraph와 Agent로 넘어가기 전에 `@tool`, `bind_tools`가 어떤 역할을 하는지 최소 수준으로만 다룹니다.

## 파일별 역할

| 파일 | 내용 |
| --- | --- |
| `01_langchain_tool_decorator.py` | `@tool`로 Python 함수를 Tool 객체로 만드는 방법을 확인합니다. |
| `02_bind_tools_basic.py` | ChatOpenAI에 Tool을 바인딩하고 모델이 Tool 호출을 제안하는 흐름을 확인합니다. |

## 실행

```powershell
cd C:\aidev\05_llm-agent-orchestration\04_function-calling-and-tool-use
.\.venv\Scripts\Activate.ps1
python .\04_langchain-tool-binding\01_langchain_tool_decorator.py
python .\04_langchain-tool-binding\02_bind_tools_basic.py
```

`02_bind_tools_basic.py`는 OpenAI API Key가 있어야 실제 모델 호출을 진행합니다. API Key가 없으면 안전하게 종료됩니다.

## 확인 질문

- `@tool`은 일반 Python 함수를 어떻게 바꾸어 주나요?
- Tool 설명과 입력값 타입 힌트가 중요한 이유는 무엇인가요?
- 모델이 Tool을 선택하더라도 실제 실행은 누가 담당하나요?
