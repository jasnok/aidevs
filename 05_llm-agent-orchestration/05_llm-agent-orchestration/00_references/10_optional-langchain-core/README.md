# 선택 참고 · LangChain Core

LangChain은 필수 과정에서 사용하지 않습니다. Prompt, Pydantic Structured Output,
Tool, RAG, LangGraph는 각 공식 SDK와 일반 Python 코드로 먼저 학습합니다.

다음 경우에만 이 폴더를 선택적으로 확인합니다.

- 여러 Provider를 LangChain의 공통 Model Interface로 바꾸어 보고 싶을 때
- `Runnable`과 LCEL의 `|` 연결 문법을 비교하고 싶을 때
- 기존 LangChain 프로젝트를 읽어야 할 때

## 설치

공통 `requirements.txt`에는 LangChain을 넣지 않습니다.

```powershell
pip install -r .\requirements.txt
```

## 실행

```powershell
python .\01_concept_example.py
python .\02_travel_example.py
python .\03_multi_provider_chain.py
python .\04_structured_chain_comparison.py
```

이 자료는 Mini Agent 필수 메뉴에 연결하지 않으며 과제와 평가 범위에도 포함하지
않습니다.
