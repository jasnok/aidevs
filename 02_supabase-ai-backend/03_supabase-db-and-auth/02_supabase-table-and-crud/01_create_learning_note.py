r"""learning_notes 생성 예제입니다.

실행:
    cd C:\aidev\02_supabase-ai-backend
    .\.venv\Scripts\Activate.ps1
    python .\03_supabase-db-and-auth\02_supabase-table-and-crud\01_create_learning_note.py
"""

from supabase_client import get_supabase


def main() -> None:
    """learning_notes 테이블에 메모 1개를 생성합니다."""

    supabase = get_supabase()

    # insert는 SQL의 INSERT INTO와 비슷합니다.
    # 딕셔너리의 key는 테이블 컬럼명과 같아야 합니다.
    result = (
        supabase.table("learning_notes")
        .insert(
            {
                "title": "Supabase create practice",
                "content": "01_create_learning_note.py에서 생성한 학습 메모입니다.",
            }
        )
        .execute()
    )

    if not result.data:
        raise RuntimeError("insert 결과가 비어 있습니다. learning_notes 테이블과 권한을 확인하세요.")

    created = result.data[0]
    print("[created note]")
    print(f"id: {created.get('id')}")
    print(f"title: {created.get('title')}")
    print(f"content: {created.get('content')}")
    print(f"created_at: {created.get('created_at')}")


if __name__ == "__main__":
    main()
