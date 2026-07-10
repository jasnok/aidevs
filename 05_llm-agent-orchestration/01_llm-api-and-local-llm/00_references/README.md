# 00_references

이 문서는 `01_llm-api-and-local-llm` 단원을 진행할 때 함께 보는 짧은 개념 정리입니다.

## 이 단원에서 비교하는 두 가지 방식

```text
OpenAI API 호출
-> Python 코드가 인터넷을 통해 OpenAI 서버에 요청을 보냅니다.
-> 모델 실행은 OpenAI 서버에서 이루어집니다.
-> API Key와 사용량 관리가 필요합니다.

Ollama/Llama 호출
-> Docker 컨테이너 안에서 Ollama 서버를 실행합니다.
-> Python 코드가 내 PC의 localhost:11434로 요청을 보냅니다.
-> 모델 실행은 내 PC 자원을 사용합니다.
```

## .env 파일을 사용하는 이유

API Key 같은 민감한 값은 코드에 직접 적지 않습니다.

코드에 직접 적으면 다음 문제가 생깁니다.

- GitHub에 실수로 올라갈 수 있습니다.
- 키를 바꿀 때마다 코드를 수정해야 합니다.
- 여러 사람이 같은 코드를 사용할 때 개인별 설정을 분리하기 어렵습니다.

그래서 이 단원에서는 `.env.example`을 `.env`로 복사한 뒤, 실제 값은 `.env`에만 입력합니다.

```text
.env.example -> 공유 가능한 예시 파일
.env         -> 내 PC에서만 사용하는 실제 설정 파일
```

## OpenAI API Key가 없을 때

OpenAI API Key가 없으면 OpenAI 호출 예제는 건너뜁니다.

그래도 다음 실습은 진행할 수 있습니다.

- Docker Desktop 실행 확인
- Ollama 컨테이너 실행
- Llama 모델 다운로드
- Python에서 Ollama REST API 호출
- OpenAI와 Llama 비교 예제에서 Llama 쪽 결과만 확인

## Docker/Ollama/Llama 관계

```text
Docker Desktop
-> Windows에서 컨테이너를 실행할 수 있게 해주는 프로그램

Ollama 컨테이너
-> Llama 모델을 실행하는 로컬 LLM 서버

Llama 모델
-> 실제로 텍스트를 생성하는 로컬 LLM
```

이 단원에서는 Ollama를 Windows에 직접 설치하지 않습니다. Docker Desktop에서 Ollama 컨테이너를 실행해서 사용합니다.

## 결과 비교 기준

모델 비교는 “어느 모델이 무조건 더 좋다”를 찾는 활동이 아닙니다.

다음 기준으로 비교합니다.

- 응답 속도
- 설명의 정확성
- 설명의 친절함
- 출력 형식을 잘 지키는지
- 비용 또는 PC 자원 사용
- 이후 Agent 프로젝트에 연결하기 쉬운지

## 다음 단원과의 연결

이 단원에서는 LLM을 “한 번 호출하는 방법”을 배웁니다.

다음 단원부터는 같은 LLM 호출을 더 잘 쓰기 위해 다음 내용을 배웁니다.

```text
02_prompt-and-response-quality
-> 프롬프트를 역할, 지시문, 맥락으로 나누고 출력 형식을 제어합니다.

04_function-calling-and-tool-use
-> LLM이 직접 답하지 않고 필요한 도구를 호출하게 만듭니다.

05_rag-memory-and-vector-search
-> LLM이 외부 문서를 검색한 뒤 그 결과를 참고해 답하게 만듭니다.

06_langgraph-state-flow
-> 여러 단계의 판단 흐름을 상태 그래프로 관리합니다.
```
