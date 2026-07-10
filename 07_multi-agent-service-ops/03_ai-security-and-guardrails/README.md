# 03 AI Security And Guardrails

이 단원은 AI 서비스와 Multi-Agent 시스템에서 필요한 보안과 가드레일을 학습합니다.

AI 서비스는 사용자의 자연어 입력을 모델과 Agent가 해석합니다. 그래서 일반 API보다 Prompt Injection, 위험한 Tool 실행, 정책 위반 응답, 민감 정보 노출 같은 문제가 발생하기 쉽습니다.

## 학습 목표

- Prompt Injection이 무엇인지 이해하고 기본 방어 구조를 만듭니다.
- 입력 검증과 출력 필터링의 차이를 설명합니다.
- 정책 기반 응답 검증 구조를 설계합니다.
- Tool 실행 권한을 Agent 역할별로 제한합니다.
- Multi-Agent 환경에서 Agent별 접근 권한을 설계합니다.
- AI 서비스 보안 운영 가이드라인을 작성합니다.
- 감사 로그와 정책 위반 이력을 추적합니다.
- Guardrails AI 같은 검증 도구의 통합 위치를 설명합니다.

## 폴더 구조

```text
03_ai-security-and-guardrails
├─ 01_prompt-injection-defense
├─ 02_policy-based-response-validation
├─ 03_tool-permission-control
├─ 04_multi-agent-access-control
├─ 10_labs
└─ 20_assignments
```

## 기본 방어 흐름

```text
사용자 입력
-> 입력 검증
-> Prompt Injection 여부 확인
-> Agent 실행
-> Tool 권한 확인
-> 응답 정책 검증
-> 감사 로그 기록
```

## 실행 예시

```powershell
cd C:\aidev\07_multi-agent-service-ops\03_ai-security-and-guardrails
python .\01_prompt-injection-defense\01_prompt-injection-filter.py
python .\02_policy-based-response-validation\01_policy-response-validator.py
python .\03_tool-permission-control\01_tool-permission-control.py
python .\04_multi-agent-access-control\01_multi-agent-access-control.py
```

## 운영 관점에서 중요한 기준

- 차단한 입력은 이유와 함께 기록합니다.
- 정책 위반 응답은 사용자에게 그대로 보여주지 않습니다.
- 모든 Agent가 모든 Tool을 실행할 수 있으면 위험합니다.
- 민감 정보가 로그에 남지 않도록 마스킹 기준을 둡니다.
- Guardrail은 모델 호출 전과 후에 모두 둘 수 있습니다.
