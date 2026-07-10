# 04_prompt-safety-and-evaluation

이 챕터에서는 Prompt Injection을 이해하고 프롬프트 버전별 품질을 비교합니다.

## 핵심 개념

- Prompt Injection은 사용자가 시스템 지시문을 무시하게 만들려는 공격입니다.
- 입력 검증은 위험한 요청을 먼저 걸러내는 과정입니다.
- 프롬프트 버전 평가는 어떤 프롬프트가 더 안정적인지 비교하는 과정입니다.
- 안전한 Agent를 만들려면 사용자의 입력을 지시문이 아니라 데이터로 구분해 다루어야 합니다.

## 실행 순서

```powershell
cd C:\aidev\05_llm-agent-orchestration\02_prompt-and-response-quality
.\.venv\Scripts\Activate.ps1
python .\04_prompt-safety-and-evaluation\01_prompt-injection-defense.py
python .\04_prompt-safety-and-evaluation\02_prompt-version-evaluation.py
```

## 파일별 역할

| 파일 | 역할 |
| --- | --- |
| `01_prompt-injection-defense.py` | 위험한 사용자 입력을 데이터로 감싸고 안전성 분류 응답을 요청합니다. |
| `02_prompt-version-evaluation.py` | 프롬프트 버전별 응답을 비교하고 평가 기준을 확인합니다. |

## 관찰할 내용

- 위험 입력을 그대로 따르지 않는가?
- 시스템 규칙과 사용자 입력이 명확히 구분되는가?
- 프롬프트 버전이 바뀌면 응답 품질이 어떻게 달라지는가?

## 확인 질문

- 사용자의 입력을 그대로 믿으면 어떤 문제가 생길까요?
- 프롬프트 품질은 어떤 기준으로 평가할 수 있을까요?
- 위험 입력을 완전히 막기 위해 프롬프트만으로 충분할까요?
