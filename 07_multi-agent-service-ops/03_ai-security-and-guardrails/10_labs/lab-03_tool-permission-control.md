# Lab 03. Tool Permission Control

## 목표

Agent 역할별 Tool 실행 권한을 제한합니다.

## 실행

```powershell
cd C:\aidev\07_multi-agent-service-ops\03_ai-security-and-guardrails
python .\03_tool-permission-control\01_tool-permission-control.py
```

## 작성할 내용

| Agent | 허용 Tool | 금지 Tool | 이유 |
| --- | --- | --- | --- |
| viewer_agent | | | |
| ops_agent | | | |
| admin_agent | | | |

## 확인 질문

- 권한 위반을 어떻게 기록할 것인가?
- Tool 실행 전과 후 중 어디에서 권한을 검사할 것인가?
