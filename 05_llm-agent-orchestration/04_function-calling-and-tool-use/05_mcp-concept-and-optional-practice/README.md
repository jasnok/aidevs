# 05_mcp-concept-and-optional-practice

이 챕터에서는 MCP 개념을 Function Calling과 비교하면서 이해합니다.

## 핵심 개념

- MCP는 Model Context Protocol의 줄임말입니다.
- LLM이 외부 도구와 데이터 소스에 연결되는 방식을 표준화하려는 개념입니다.
- 이 단원에서는 MCP를 먼저 Tool Use와 비교하고, 간단한 선택 실습 수준으로 다룹니다.

## 실행

```powershell
cd C:\aidev\05_llm-agent-orchestration\04_function-calling-and-tool-use
.\.venv\Scripts\Activate.ps1
python .\05_mcp-concept-and-optional-practice\01_mcp-concept-summary.py
```

간단한 MCP 서버/클라이언트 실습은 선택입니다.

```powershell
pip install mcp
python .\05_mcp-concept-and-optional-practice\03_mcp_client_test.py
```

`03_mcp_client_test.py`는 내부에서 `02_simple_mcp_server.py`를 stdio 방식으로 실행한 뒤 `course_search` Tool을 호출합니다.

## 파일별 역할

| 파일 | 내용 |
| --- | --- |
| `01_mcp-concept-summary.py` | Function Calling, Tool Use, MCP 차이를 표로 확인합니다. |
| `02_simple_mcp_server.py` | `course_search` Tool 하나를 제공하는 작은 MCP 서버입니다. |
| `03_mcp_client_test.py` | MCP 서버에 연결해 Tool 목록을 보고 Tool을 호출합니다. |

## 확인 질문

- Function Calling과 MCP는 어떤 공통점이 있나요?
- MCP가 필요한 상황은 어떤 경우일까요?
- MCP 서버가 제공하는 Tool과 일반 Python 함수 Tool은 어떤 점이 다른가요?
