# 04 OpenAI API Key and Cost Safety

OpenAI API Key는 매우 중요합니다. API Key는 서비스 사용 권한을 가진 비밀번호와 비슷합니다.

## 반드시 지킬 것

- API Key를 코드에 직접 쓰지 않는다.
- API Key를 GitHub에 올리지 않는다.
- API Key를 화면 캡처에 노출하지 않는다.
- `.env` 파일에 저장한다.
- `.env.example`에는 예시 값만 넣는다.
- 유출되었다면 즉시 삭제하고 새로 만든다.

## 좋은 방식

`.env` 파일:

```text
OPENAI_API_KEY=your-real-api-key
OPENAI_MODEL=gpt-4.1-mini
```

Python 코드:

```python
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()
```

OpenAI SDK는 환경 변수의 `OPENAI_API_KEY`를 자동으로 읽을 수 있습니다.

## 나쁜 방식

```python
client = OpenAI(api_key="sk-실제키값")
```

이런 방식은 코드 공유나 GitHub 업로드 시 키 유출 위험이 큽니다.

## 비용 관리

API는 사용량에 따라 비용이 발생할 수 있습니다.

수업에서는 다음 원칙을 권장합니다.

- 필요할 때만 예제를 실행한다.
- 긴 문서를 무작정 많이 보내지 않는다.
- embedding 실습은 작은 문서로 시작한다.
- 반복 실행이 필요한 예제는 Mock 데이터를 먼저 사용한다.
- 팀 프로젝트에서는 호출 횟수를 줄이는 구조를 고민한다.

## 비용이 발생하기 쉬운 구간

- 많은 문서 chunk에 embedding을 생성할 때
- RAG 검색 후 긴 context를 넣을 때
- Streamlit 버튼을 여러 번 눌러 API를 반복 호출할 때
- 팀원 여러 명이 같은 API Key를 공유해 많이 실행할 때

## 수업 운영 팁

수업 진행에서는 다음을 미리 안내하는 것이 좋습니다.

```text
API Key는 개인별로 관리한다.
실습 전 호출 횟수를 설명한다.
API Key가 없어도 실행 가능한 Mock 예제를 먼저 사용한다.
실제 LLM 호출은 핵심 예제에서만 진행한다.
```
