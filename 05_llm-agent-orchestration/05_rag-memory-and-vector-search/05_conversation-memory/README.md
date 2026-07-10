# 05 Conversation Memory

이 폴더에서는 Agent가 이전 대화를 기억하고 다음 응답에 활용하는 구조를 학습합니다.

## 핵심 개념

- Session Memory는 현재 대화 흐름을 유지하기 위한 짧은 기억입니다.
- PostgreSQL Session Memory는 대화 이력을 테이블에 저장해 다시 조회할 수 있게 합니다.
- Redis Session Cache는 빠르게 읽고 쓰는 임시 기억입니다.
- Long-term Memory는 나중에 다시 검색할 수 있도록 벡터로 저장하는 장기 기억입니다.
- Agent는 Memory를 통해 더 일관된 답변과 개인화된 응답을 만들 수 있습니다.

## 예제 파일

| 파일 | 내용 |
| --- | --- |
| `01_short-term-memory.py` | Python 리스트로 짧은 대화 기억 흐름을 확인합니다. |
| `02_save-conversation-memory.py` | 대화 내용을 DB에 저장하는 구조를 실습합니다. |
| `03_load-recent-session-messages.py` | 특정 session_id의 최근 대화를 DB에서 불러옵니다. |
| `04_redis-session-cache.py` | Redis에 최근 대화 캐시를 저장하고 읽습니다. |

## 실행

```powershell
cd C:\aidev\05_llm-agent-orchestration\05_rag-memory-and-vector-search
.\.venv\Scripts\Activate.ps1
python .\05_conversation-memory\01_short-term-memory.py
python .\05_conversation-memory\02_save-conversation-memory.py
python .\05_conversation-memory\03_load-recent-session-messages.py
python .\05_conversation-memory\04_redis-session-cache.py
```

## 확인 질문

- 모든 대화를 그대로 저장하면 어떤 문제가 생길 수 있는가?
- 요약 메모리는 어떤 상황에서 유용한가?
- Session Memory와 Long-term Memory를 함께 쓰면 어떤 장점이 있는가?
