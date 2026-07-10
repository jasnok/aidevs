# 03 Tool Permission Control

Tool 실행 권한 제어는 Agent가 어떤 도구를 사용할 수 있는지 제한하는 구조입니다.

## 필요한 이유

모든 Agent가 모든 Tool을 실행할 수 있으면 위험합니다.

예를 들어 `viewer_agent`는 로그 조회만 가능해야 하고, `ops_agent`만 재시작 요청을 만들 수 있어야 합니다.

## 기본 흐름

```text
Agent 역할 확인
-> 요청한 Tool 확인
-> 권한 검사
-> 허용된 경우만 실행
-> 실행 결과와 권한 판단 로그 기록
```

## 실행

```powershell
cd C:\aidev\07_multi-agent-service-ops\03_ai-security-and-guardrails
python .\03_tool-permission-control\01_tool-permission-control.py
```

## 확인할 것

- Agent별 허용 Tool 목록이 있는가?
- 허용되지 않은 Tool 실행을 차단하는가?
- 권한 위반 로그가 남는가?
