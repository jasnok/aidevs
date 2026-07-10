# 03 LangChain Basics

이 단원은 LangChain을 사용해 프롬프트, 모델, 출력 파서, 문서 처리를 하나의 실행 흐름으로 연결하는 방법을 학습합니다.

LangChain은 05 과정에서 깊게 다루는 필수 프레임워크라기보다, LLM 호출 흐름을 구조화해서 이해하기 위한 최소 도구입니다. 초보자는 먼저 직접 API 호출 방식을 이해한 뒤 LangChain이 어떤 반복 작업을 줄여주는지 비교하면서 보면 좋습니다.

이 단원에서 기억할 기준은 다음입니다.

```text
직접 API 호출
-> 작은 예제에서는 가장 단순하고 이해하기 쉽습니다.

LangChain
-> 프롬프트, 모델, 출력 파서, 문서 처리 단계를 반복적으로 연결할 때 유용합니다.
```

## 학습 목표

- 직접 LLM을 호출하는 방식과 LangChain을 사용하는 방식을 비교합니다.
- PromptTemplate과 ChatPromptTemplate의 역할을 이해합니다.
- LCEL과 Runnable Chain의 기본 실행 흐름을 익힙니다.
- Structured Output과 Pydantic 결과 검증을 연습합니다.
- 문서를 읽고 chunk로 나누는 RAG 전처리 흐름을 이해합니다.

## 폴더 구성

```text
03_langchain-minimal
├─ .env.example
├─ 00_references
│  └─ README.md
├─ 01_langchain-overview
│  ├─ README.md
│  └─ 01_direct-call-vs-langchain.py
├─ 02_prompt-template-and-output-parser
│  ├─ README.md
│  ├─ 01_prompt-template-basic.py
│  ├─ 02_chat-prompt-template.py
│  └─ 03_structured-output-parser.py
├─ 03_chain-and-runnable
│  ├─ README.md
│  ├─ 01_simple-runnable-chain.py
│  └─ 02_batch-and-stream.py
├─ 04_document-loader-and-text-splitter
│  ├─ README.md
│  ├─ 01_load-text-document.py
│  └─ 02_split-documents.py
├─ 10_labs
└─ 20_assignments
```

## 실습 시작 순서

```powershell
cd C:\aidev\05_llm-agent-orchestration\03_langchain-minimal
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install langchain langchain-openai langchain-core langchain-text-splitters python-dotenv pydantic
Copy-Item .env.example .env
```

이 단원의 `.env`는 `C:\aidev\05_llm-agent-orchestration\03_langchain-minimal\.env` 파일입니다. 01, 02 단원의 `.env`를 자동으로 읽지 않습니다.

## 실행 순서

```powershell
python .\01_langchain-overview\01_direct-call-vs-langchain.py
python .\02_prompt-template-and-output-parser\01_prompt-template-basic.py
python .\02_prompt-template-and-output-parser\02_chat-prompt-template.py
python .\02_prompt-template-and-output-parser\03_structured-output-parser.py
python .\03_chain-and-runnable\01_simple-runnable-chain.py
python .\03_chain-and-runnable\02_batch-and-stream.py
python .\04_document-loader-and-text-splitter\01_load-text-document.py
python .\04_document-loader-and-text-splitter\02_split-documents.py
```

## 단원별 핵심 연결

| 폴더 | 핵심 질문 |
| --- | --- |
| `01_langchain-overview` | 직접 호출과 LangChain 호출은 무엇이 다른가? |
| `02_prompt-template-and-output-parser` | 프롬프트와 출력 파서를 어떻게 구조화하는가? |
| `03_chain-and-runnable` | 데이터가 체인 안에서 어떤 순서로 이동하는가? |
| `04_document-loader-and-text-splitter` | RAG를 위해 문서를 어떻게 나누어 준비하는가? |

## 수업 중 확인 질문

- 직접 API 호출과 LangChain 호출은 어떤 점이 다른가요?
- PromptTemplate은 단순 문자열 조합과 무엇이 다른가요?
- Runnable Chain은 입력이 어떤 순서로 이동하나요?
- 문서를 chunk로 나누는 이유는 무엇인가요?
