# Lab 03. Supervisor Routing

## 목표

Supervisor가 요청 유형에 따라 담당 Agent를 선택하는 흐름을 이해합니다.

## 실행

```powershell
cd C:\aidev\07_multi-agent-service-ops\01_multi-agent-collaboration
python .\03_supervisor-router-workflow\01_supervisor-router-workflow.py
```

## 작성할 내용

```text
장애 요청 -> diagnosis_agent
복구 요청 -> recovery_agent
검증 요청 -> validation_agent
로그 요청 -> reporter_agent
```

새로운 요청 유형을 하나 추가하고, 어떤 Agent가 처리해야 하는지 정리합니다.
