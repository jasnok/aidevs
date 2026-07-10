# 03_multi-tool-orchestration

이 챕터에서는 여러 Tool 중 필요한 Tool을 선택하고 결과를 통합하는 흐름을 학습합니다.

## 핵심 개념

- Multi-Tool Agent는 요청에 따라 서로 다른 Tool을 선택합니다.
- Router는 어떤 Tool을 사용할지 결정하는 역할을 합니다.
- Tool 결과를 모아 최종 응답을 만드는 과정이 오케스트레이션입니다.

## 실행

```powershell
cd C:\aidev\05_llm-agent-orchestration\04_function-calling-and-tool-use
.\.venv\Scripts\Activate.ps1
python .\03_multi-tool-orchestration\01_multi-tool-router.py
python .\03_multi-tool-orchestration\02_manual-tool-selection-flow.py
```

## 확인 질문

- Tool 선택 기준은 어디에 정의해야 할까요?
- Tool 결과가 서로 충돌하면 어떻게 처리해야 할까요?

