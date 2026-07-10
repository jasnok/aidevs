# 01 Single Vs Multi Agent

이 실습은 단일 Agent와 Multi-Agent 구조를 비교합니다.

## 핵심 개념

| 구조 | 특징 |
| --- | --- |
| Single Agent | 하나의 Agent가 분석, 실행, 검증을 모두 처리합니다. |
| Multi-Agent | 여러 Agent가 역할을 나누어 협업합니다. |

단일 Agent는 구조가 단순하지만, 작업이 복잡해지면 책임이 많아지고 디버깅이 어려워질 수 있습니다. Multi-Agent는 설계가 조금 더 복잡하지만 역할 분리와 결과 검증이 쉬워집니다.

## 실행

```powershell
cd C:\aidev\07_multi-agent-service-ops\01_multi-agent-collaboration
python .\01_single-vs-multi-agent\01_single-agent-vs-multi-agent.py
```

## 확인할 것

- 단일 Agent가 처리하는 단계가 무엇인지 확인합니다.
- Multi-Agent에서 역할이 어떻게 나뉘는지 확인합니다.
- 어떤 구조가 장애 대응과 로그 분석에 더 유리한지 생각합니다.
