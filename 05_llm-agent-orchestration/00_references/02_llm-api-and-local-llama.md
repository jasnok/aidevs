# 02 LLM API and Local Llama

이 과정에서는 두 종류의 LLM 사용 방식을 배웁니다.

```text
필수 클라우드 LLM: OpenAI API
필수 로컬 LLM: Llama via Docker/Ollama
```

## OpenAI API

OpenAI API는 인터넷을 통해 OpenAI 서버의 모델을 호출하는 방식입니다.

장점:

- 실습 예제가 많다.
- 응답 품질이 안정적이다.
- Function Calling, Structured Output, LangChain, LangGraph와 연결하기 쉽다.
- 수업의 메인 모델로 사용하기 좋다.

주의할 점:

- API Key가 필요하다.
- 사용량에 따라 비용이 발생할 수 있다.
- API Key를 코드나 GitHub에 올리면 안 된다.

## 로컬 Llama

로컬 Llama는 Docker/Ollama를 사용해 내 PC에서 Llama 모델을 실행하는 방식입니다.

장점:

- 로컬 LLM이 어떻게 실행되는지 이해할 수 있다.
- API 비용 없이 일부 실습을 해볼 수 있다.
- 클라우드 API와 로컬 모델의 차이를 비교할 수 있다.

주의할 점:

- PC 사양에 따라 느릴 수 있다.
- 모델 다운로드에 시간이 걸릴 수 있다.
- 큰 모델은 실행이 어렵거나 매우 느릴 수 있다.

## 수업에서의 역할 분리

```text
OpenAI API
-> 기본 실습 모델
-> Function Calling
-> Structured Output
-> RAG 답변 생성
-> LangChain/LangGraph 실습

Llama via Docker/Ollama
-> 로컬 모델 실행 경험
-> OpenAI와 응답 비교
-> 비용과 성능 차이 이해
```

## 처음부터 여러 모델을 많이 쓰지 않는 이유

초보자 과정에서 모델을 너무 많이 쓰면 학습 초점이 흐려집니다.

모델별 API Key, SDK, 오류, 응답 형식이 달라지면 에이전트 구조보다 설정 문제에 시간을 쓰게 됩니다.

그래서 이 과정에서는 다음 기준을 사용합니다.

```text
기본 구현: OpenAI API
비교 실습: Llama via Docker/Ollama
```
