# Lab 05. Handoff Context MCP

## 목표

Agent 간 업무 인계, Context 공유, Context 동기화 기준을 설계합니다.

## 실행

```powershell
cd C:\aidev\07_multi-agent-service-ops\01_multi-agent-collaboration
python .\05_handoff-context-mcp\01_handoff_context_mcp.py
```

## 작성할 내용

1. Agent 역할 목록
2. Handoff 순서
3. 다음 Agent에게 넘길 Context
4. Agent별 허용 Tool
5. 민감 정보가 Context에 포함될 때 처리 기준
6. Agent 간 Context 동기화 기준
7. Handoff 실패 시 fallback 기준

## 확인 질문

- 전체 대화를 모두 넘기는 것과 필요한 Context만 넘기는 것의 차이는 무엇인가?
- Context 동기화에 반드시 필요한 필드는 무엇인가?
- MCP 같은 외부 도구 연결 구조에서 권한 검사는 어디에 있어야 하는가?
