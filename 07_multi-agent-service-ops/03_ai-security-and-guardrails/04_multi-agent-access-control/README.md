# 04 Multi Agent Access Control

이 실습은 Multi-Agent 환경에서 Agent별 접근 범위를 제한하는 방법을 다룹니다.

## 접근 제어 대상

| 대상 | 예시 |
| --- | --- |
| 데이터 | 로그, 사용자 정보, 장애 이력 |
| Tool | 조회, 재시도, 재시작, 배포 |
| Context | Handoff 시 전달 가능한 정보 |
| Secret | API Key, AWS Key, DB 비밀번호 |

## 실행

```powershell
cd C:\aidev\07_multi-agent-service-ops\03_ai-security-and-guardrails
python .\04_multi-agent-access-control\01_multi-agent-access-control.py
```

## 확인할 것

- Agent 역할별 접근 범위가 정의되어 있는가?
- 민감 Context가 필요 이상으로 전달되지 않는가?
- 권한 위반 이력이 감사 로그로 남는가?
