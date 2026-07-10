# 02 OpenAI and Ollama Errors

## OpenAI API Key 오류

확인:

```powershell
Get-Content .env
```

실제 수업 중에는 API Key를 화면 공유하거나 제출물에 포함하지 않습니다.

확인할 항목:

- `.env` 파일이 현재 단원 폴더에 있는가?
- `OPENAI_API_KEY=` 이름이 정확한가?
- 가상환경에 `openai`, `python-dotenv`가 설치되어 있는가?

## Ollama 연결 오류

확인:

```powershell
docker ps
docker exec -it ollama-llm ollama list
```

모델이 없다면:

```powershell
docker exec -it ollama-llm ollama pull llama3.2
```

Ollama는 선택 실습입니다. PC 사양이나 시간이 부족하면 OpenAI 또는 mock 예제로 진행해도 됩니다.
