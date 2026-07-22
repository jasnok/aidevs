r"""Notes API 구조화 예제의 시작 파일입니다.

실행:
    cd C:\aidev\02_supabase-ai-backend\03_supabase-db-and-auth\90_structured-fastapi-examples\01_notes-api-with-supabase
    uvicorn app.main:app --reload --host 127.0.0.1 --port 8011
    # 위 명령에서 오류가 나면 아래처럼 실행합니다.
    python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8011
"""

from fastapi import FastAPI

from app.routers.notes_router import router as notes_router


# app은 FastAPI 애플리케이션의 시작 객체입니다.
# uvicorn app.main:app 명령에서 마지막 app이 바로 이 변수입니다.
app = FastAPI(title="Example 01 - Notes API With Supabase")

# router를 분리하면 main.py는 앱 조립만 담당하고,
# 실제 endpoint 코드는 app/routers/notes_router.py에서 관리할 수 있습니다.
app.include_router(notes_router)
