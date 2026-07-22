# 01. Notes API With Supabase

`learning_notes` CRUD 흐름을 실제 프로젝트 구조처럼 나누어 보는 예제입니다.

본문의 `02_supabase-table-and-crud`, `03_fastapi-supabase-integration`을 구조화한 버전입니다.

## 이 예제에서 배우는 것

- FastAPI 코드를 `main`, `router`, `schema`, `service`, `config`로 나누는 방법
- Supabase 테이블 CRUD를 service 함수로 분리하는 방법
- 본문 실습 테이블과 섞이지 않도록 `ex90_notes` 테이블을 사용하는 방법

## 1. Supabase 테이블 만들기

Supabase SQL Editor에서 이 폴더의 `schema.sql`을 실행합니다.

```text
C:\aidev\02_supabase-ai-backend\03_supabase-db-and-auth\90_structured-fastapi-examples\01_notes-api-with-supabase\schema.sql
```

실행되는 SQL은 아래처럼 `ex90_notes` 테이블을 만듭니다.

```sql
create table if not exists ex90_notes (
  id uuid primary key default gen_random_uuid(),
  title text not null,
  content text not null,
  created_at timestamptz not null default now()
);
```

이 예제는 본문 실습의 `learning_notes`가 아니라 `ex90_notes`를 사용합니다. 따라서 `learning_notes`가 이미 있어도 `ex90_notes`를 따로 만들어야 합니다.

## 2. 환경변수 준비

`.env.example`을 참고해 같은 폴더에 `.env`를 만듭니다.

```text
SUPABASE_URL=...
SUPABASE_SERVICE_ROLE_KEY=...
```

이 예제에는 `SUPABASE_ANON_KEY`를 사용하지 않습니다. 로그인한 사용자 권한으로 RLS를 확인하는 예제가 아니라, FastAPI 서버가 서버 권한으로 `ex90_notes` 테이블을 CRUD하는 구조이기 때문입니다.

`SUPABASE_SERVICE_ROLE_KEY`는 RLS를 우회할 수 있는 서버 전용 관리자 key입니다. GitHub, README, 제출 문서, 화면 캡처에 노출하지 않습니다.

## 3. 서버 실행

```powershell
cd C:\aidev\02_supabase-ai-backend\03_supabase-db-and-auth\90_structured-fastapi-examples\01_notes-api-with-supabase
..\..\..\.venv\Scripts\Activate.ps1
python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8011
```

Swagger UI:

```text
http://127.0.0.1:8011/docs
```

## 확인할 endpoint

| Method | URL | 설명 |
|---|---|---|
| GET | `/health` | 서버와 환경변수 상태 확인 |
| GET | `/notes` | 노트 목록 조회 |
| POST | `/notes` | 노트 생성 |
| GET | `/notes/{note_id}` | 노트 1개 조회 |
| PUT | `/notes/{note_id}` | 노트 수정 |
| DELETE | `/notes/{note_id}` | 노트 삭제 |

## 테스트

```powershell
python -m pytest tests
```

테스트는 외부 Supabase를 호출하지 않고 앱의 기본 라우트가 준비되었는지만 확인합니다.

## 자주 나는 오류

### `Could not find the table 'public.ex90_notes'`

Supabase에 `ex90_notes` 테이블이 없을 때 발생합니다.

해결 방법:

1. Supabase Dashboard로 이동합니다.
2. SQL Editor를 엽니다.
3. 이 폴더의 `schema.sql` 내용을 실행합니다.
4. 서버를 다시 실행하거나 Swagger에서 API를 다시 호출합니다.

PostgREST schema cache 때문에 방금 만든 테이블이 바로 보이지 않는 경우가 드물게 있습니다. 그럴 때는 Supabase Dashboard에서 잠시 기다린 뒤 다시 호출하거나 서버를 재시작합니다.

## 바이브 코딩으로 endpoint 테스트 만들기

기본 테스트는 `tests/test_app_routes.py`만 실행합니다. 전체 endpoint 흐름까지 확인하는 테스트는 수업 중 필수가 아니라, Codex와 함께 만들어 보는 선택 실습으로 둡니다.

참고 예시는 아래 파일에 있습니다.

```text
tests/reference_api_flow_example.py
```

이 파일 상단에는 Codex에게 보낼 수 있는 프롬프트 예시가 들어 있습니다. 실제로 실행하고 싶다면 아래처럼 복사합니다.

```powershell
Copy-Item .\tests\reference_api_flow_example.py .\tests\test_api_flow.py
python -m pytest tests
```
