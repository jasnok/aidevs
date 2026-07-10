# Lab 04. Multi Agent Access Control

## 목표

Multi-Agent 환경에서 데이터, Tool, Context 접근 범위를 정리합니다.

## 실행

```powershell
cd C:\aidev\07_multi-agent-service-ops\03_ai-security-and-guardrails
python .\04_multi-agent-access-control\01_multi-agent-access-control.py
```

## 작성할 내용

- Agent별 접근 가능한 데이터
- Agent별 실행 가능한 Tool
- Handoff 시 전달 가능한 Context
- 민감 정보 마스킹 기준

## 확인 질문

- 모든 Agent가 같은 Context를 볼 필요가 있는가?
- 어떤 Agent에게 재시작 Tool 권한을 줄 것인가?
- 권한 위반 이벤트는 어디에 기록할 것인가?
