r"""learning_notes 수정 예제입니다.

실행:
    cd C:\aidev\02_supabase-ai-backend
    .\.venv\Scripts\Activate.ps1
    python .\03_supabase-db-and-auth\02_supabase-table-and-crud\04_update_learning_note.py
"""

from supabase_client import get_supabase


def main() -> None:
    """실습용 메모를 만든 뒤 title/content를 수정합니다."""

    supabase = get_supabase()

    created_result = (
        supabase.table("learning_notes")
        .insert(
            {
                "title": "Supabase update practice",
                "content": "수정 전 내용입니다.",
            }
        )
        .execute()
    )

    if not created_result.data:
        raise RuntimeError("수정 실습용 메모를 생성하지 못했습니다.")

    created = created_result.data[0]
    note_id = created["id"]
    print(f"[created for update]\nid: {note_id}")

    # update에는 조건이 중요합니다.
    # eq("id", note_id)를 붙여야 방금 만든 메모 1개만 수정됩니다.
    updated_result = (
        supabase.table("learning_notes")
        .update(
            {
                "title": "Supabase update practice - updated",
                "content": "04_update_learning_note.py에서 수정한 내용입니다.",
            }
        )
        .eq("id", note_id)
        .execute()
    )

    if not updated_result.data:
        raise RuntimeError("update 결과가 비어 있습니다. note_id와 테이블 권한을 확인하세요.")

    updated = updated_result.data[0]
    print("\n[updated note]")
    print(f"id: {updated.get('id')}")
    print(f"title: {updated.get('title')}")
    print(f"content: {updated.get('content')}")


if __name__ == "__main__":
    main()
