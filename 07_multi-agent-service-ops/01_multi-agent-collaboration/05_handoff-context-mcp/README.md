# 05 Handoff Context MCP

이 실습은 Agent 간 업무 인계(Handoff), Context 공유, MCP 기반 외부 도구 연결 개념을 다룹니다.

## Handoff란?

Handoff는 한 Agent가 처리한 결과를 다음 Agent에게 넘기는 과정입니다.

```text
Diagnosis Agent
-> 장애 원인 분석
-> Recovery Agent에게 필요한 Context 전달
```

## 전달해야 할 Context

| 항목 | 설명 |
| --- | --- |
| request_id | 같은 요청을 처리하고 있음을 나타내는 ID |
| service_name | 문제가 발생한 서비스 |
| failure_type | 장애 유형 |
| previous_result | 이전 Agent의 판단 결과 |
| allowed_tools | 다음 Agent가 사용할 수 있는 Tool |
| security_notes | 민감 정보, 권한, 정책 관련 주의 사항 |

## MCP는 어디에 연결되는가?

MCP(Model Context Protocol)는 모델이나 Agent가 외부 도구와 연결되는 구조를 표준화하려는 개념입니다. 이 과정에서는 실제 MCP 서버를 깊게 구축하기보다, 외부 도구 연결 시 Context와 권한을 어떻게 관리해야 하는지 이해합니다.

## 실행

```powershell
cd C:\aidev\07_multi-agent-service-ops\01_multi-agent-collaboration
python .\05_handoff-context-mcp\01_handoff_context_mcp.py
```

## 확인할 것

- 모든 대화 내용을 넘기는 것과 필요한 Context만 넘기는 것의 차이를 설명합니다.
- Agent 간 Context 동기화 기준을 정합니다.
- Handoff 실패 시 fallback 기준을 정합니다.
