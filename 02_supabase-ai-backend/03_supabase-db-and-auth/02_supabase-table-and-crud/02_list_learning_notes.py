r"""learning_notes 전체 조회 예제입니다.

실행:
    cd C:\aidev\02_supabase-ai-backend
    .\.venv\Scripts\Activate.ps1
    python .\03_supabase-db-and-auth\02_supabase-table-and-crud\02_list_learning_notes.py
"""

from datetime import datetime
from zoneinfo import ZoneInfo

from supabase_client import get_supabase


def main() -> None:
    """학습 메모 전체 목록을 조회합니다."""

    supabase = get_supabase()

    # select("*")는 모든 컬럼을 조회한다는 뜻입니다.
    # order("created_at", desc=True)는 최신 데이터가 먼저 보이도록 정렬합니다.
    try:
        result = (
            supabase.table("learning_notes")
            .select("*")
            .order("created_at", desc=True)
            .execute()
        )
    except:
        raise RuntimeError("DB가 없습니다.")

    print("[all learning_notes]")
    if not result.data:
        print("저장된 메모가 없습니다. 먼저 01_create_learning_note.py를 실행해 보세요.")
        return
    
    for note in result.data:
        created_at = datetime.fromisoformat(
            note["created_at"].replace("Z", "+00:00")
        )
        korean_time = created_at.astimezone(ZoneInfo("Asia/Seoul"))

        print(
            f'{note["id"]} {note["title"]} '
            f'{korean_time:%Y-%m-%d %H:%M:%S}'
        )



if __name__ == "__main__":
    main()
