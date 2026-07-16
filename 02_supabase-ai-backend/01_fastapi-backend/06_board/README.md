# FastAPI 게시판 CRUD

## 실행

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8001
```

서버 실행 후 `http://127.0.0.1:8001/docs`에서 API를 직접 확인할 수 있습니다.

## API

| Method | Path | 설명 |
|---|---|---|
| POST | `/posts` | 게시글 생성 |
| GET | `/posts?page=1&size=10` | 게시글 목록 |
| GET | `/posts/{id}` | 게시글 상세 |
| PATCH | `/posts/{id}` | 게시글 일부 수정 |
| DELETE | `/posts/{id}` | 게시글 삭제 |

## 테스트

```powershell
pytest -q
```
