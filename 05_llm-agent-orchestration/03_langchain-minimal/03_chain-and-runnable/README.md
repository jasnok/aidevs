# 03_chain-and-runnable

이 챕터에서는 LangChain의 Runnable과 Chain 흐름을 학습합니다.

## 핵심 개념

- Runnable은 입력을 받아 처리하고 출력하는 실행 단위입니다.
- Chain은 여러 실행 단위를 순서대로 연결한 구조입니다.
- Batch와 Stream은 여러 입력 처리와 응답 흐름 표시를 이해하는 데 도움이 됩니다.

## 실행

```powershell
cd C:\aidev\05_llm-agent-orchestration\03_langchain-minimal
.\.venv\Scripts\Activate.ps1
python .\03_chain-and-runnable\01_simple-runnable-chain.py
python .\03_chain-and-runnable\02_batch-and-stream.py
```

## 확인 질문

- Chain에서 데이터는 어떤 순서로 이동하나요?
- Stream 응답은 사용자 경험에 어떤 도움을 주나요?

