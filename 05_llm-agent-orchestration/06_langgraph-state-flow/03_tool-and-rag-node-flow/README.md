# 03 Tool and RAG Node Flow

이 폴더에서는 Tool 호출, RAG 검색, Memory 흐름을 LangGraph Node로 연결합니다.

## 핵심 개념

- Tool Node는 외부 기능을 실행하는 단계입니다.
- RAG Node는 질문과 관련 있는 context를 검색하는 단계입니다.
- Hybrid Memory는 Session Memory와 Vector Memory를 함께 사용하는 구조입니다.

## 예제 파일

| 파일 | 내용 |
| --- | --- |
| `01_tool-node-style-flow.py` | Tool 실행 결과를 State에 저장하는 흐름 |
| `02_mock-rag-node-flow.py` | mock RAG 검색 결과를 State에 연결하는 흐름 |
| `03_llm-answer-node.py` | LLM 답변 생성 Node 예제 |
| `04_hybrid-memory-flow.py` | Session Memory와 Vector Memory를 함께 사용하는 흐름 |

## 실행

```powershell
cd C:\aidev\05_llm-agent-orchestration\06_langgraph-state-flow
.\.venv\Scripts\Activate.ps1
python .\03_tool-and-rag-node-flow\01_tool-node-style-flow.py
python .\03_tool-and-rag-node-flow\02_mock-rag-node-flow.py
python .\03_tool-and-rag-node-flow\03_llm-answer-node.py
python .\03_tool-and-rag-node-flow\04_hybrid-memory-flow.py
```

## 확인 질문

- Tool 결과는 State의 어느 필드에 저장하는 것이 좋은가?
- RAG 결과와 Memory 결과가 충돌하면 어떤 기준으로 정리해야 하는가?
- 최종 답변 Node는 어떤 입력을 받아야 하는가?
