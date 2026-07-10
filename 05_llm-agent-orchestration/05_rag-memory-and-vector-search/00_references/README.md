# 00 References

이 문서는 `05_rag-memory-and-vector-search` 실습에서 반복해서 등장하는 개념을 정리합니다.

## Embedding

임베딩은 텍스트를 숫자 목록으로 바꾸는 과정입니다. 컴퓨터는 문장의 의미를 그대로 이해하지 못하므로, 문장을 벡터로 변환한 뒤 벡터 사이의 거리를 계산합니다.

예를 들어 “FastAPI 라우팅”과 “API 엔드포인트”는 단어가 완전히 같지 않아도 의미가 비슷합니다. 임베딩을 사용하면 이런 의미적 유사성을 계산할 수 있습니다.

## Vector DB와 pgvector

Vector DB는 벡터를 저장하고 검색하기 위한 저장소입니다. 이 과정에서는 별도 Vector DB 제품을 설치하지 않고, PostgreSQL에 `pgvector` 확장을 추가해서 사용합니다.

`pgvector`를 사용하면 다음 작업을 할 수 있습니다.

- 텍스트의 임베딩 벡터 저장
- 질문 벡터와 문서 벡터의 거리 계산
- 질문과 가장 가까운 문서 검색
- RAG 답변에 사용할 context 선택

## Chunk와 Overlap

긴 문서를 한 번에 임베딩하면 검색 품질이 떨어질 수 있습니다. 그래서 문서를 작은 조각인 chunk로 나눕니다.

`overlap`은 앞뒤 chunk가 일부 문장을 공유하도록 만드는 설정입니다. 문장이 중간에서 끊겨 의미가 사라지는 문제를 줄이기 위해 사용합니다.

## RAG

RAG는 Retrieval-Augmented Generation의 약자입니다. LLM이 바로 답하지 않고, 먼저 관련 문서를 검색한 뒤 검색 결과를 근거로 답변을 생성하는 구조입니다.

기본 흐름은 다음과 같습니다.

```text
사용자 질문 -> 질문 임베딩 -> 관련 문서 검색 -> context 구성 -> LLM 답변 생성
```

## Hybrid Search와 RRF

Hybrid Search는 키워드 검색과 벡터 검색을 함께 사용하는 방식입니다. 키워드 검색은 정확한 단어 매칭에 강하고, 벡터 검색은 의미 기반 검색에 강합니다.

RRF는 Reciprocal Rank Fusion의 약자입니다. 여러 검색 결과의 순위를 합쳐 더 안정적인 최종 순위를 만드는 방식입니다.

## Memory

Session Memory는 현재 대화 안에서만 유지되는 짧은 기억입니다. Long-term Memory는 나중에 다시 검색할 수 있도록 저장하는 장기 기억입니다.

Agent를 만들 때는 두 기억을 모두 구분해서 설계해야 합니다.

- Session Memory: 현재 대화 흐름 유지
- Long-term Memory: 사용자 선호, 반복 질문, 누적 지식 저장

## 이 단원에서 Docker를 쓰는 이유

05 과정에서는 Docker를 로컬 실습 도구 실행에 사용합니다. PostgreSQL과 pgvector를 노트북에 직접 설치하지 않고 컨테이너로 실행하면 설치 충돌을 줄이고, 같은 환경을 반복해서 만들 수 있습니다.

Docker Compose, AWS 배포, GitHub Actions 자동화는 `07_multi-agent-service-ops`에서 별도로 다룹니다.
