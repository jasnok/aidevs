"""async endpoint 예제입니다.

이 파일은 async/await 개념을 나누어 읽고 실행해 보기 위한 학습용 파일입니다.

실행:
    cd C:\aidev\02_supabase-ai-backend\01_fastapi-backend\04_async-and-external-api
    uvicorn 01_async-endpoint:app --reload
    # 위 명령에서 오류가 나면 아래처럼 실행합니다.
    python -m uvicorn 01_async-endpoint:app --reload

async def는 오래 걸리는 I/O 작업을 기다리는 동안 서버가 다른 요청을 처리할 수 있게 해줍니다.
DB 조회, 외부 API 호출, 파일 읽기 같은 작업과 함께 자주 사용합니다.
"""

# asyncio는 Python의 비동기 작업을 다룰 때 사용하는 표준 라이브러리입니다.
# 여기서는 실제 외부 API 대신 "기다리는 작업"을 흉내 내기 위해 asyncio.sleep()을 사용합니다.
import asyncio

from fastapi import FastAPI


# FastAPI 앱 객체입니다.
# uvicorn 실행 명령의 마지막 `:app`은 아래 변수 이름 `app`과 연결됩니다.
app = FastAPI(title="Async Endpoint Practice")


# async def로 만든 함수는 비동기 엔드포인트입니다.
# 오래 걸리는 작업을 await로 기다리는 동안 서버가 다른 요청도 처리할 수 있습니다.
@app.get("/slow-task")
async def slow_task(seconds: int = 2):
    """일부러 기다리는 API입니다.

    time.sleep()이 아니라 asyncio.sleep()을 사용해야 이벤트 루프를 막지 않습니다.
    """

    # await는 "이 작업이 끝날 때까지 기다리되, 서버 전체를 멈추지는 말라"는 의미입니다.
    # seconds 값을 Query Parameter로 받을 수 있습니다. 예: /slow-task?seconds=3
    await asyncio.sleep(seconds)

    return {
        "message": "slow task finished",
        "waited_seconds": seconds,
    }


@app.get("/parallel-tasks")
async def parallel_tasks():
    """여러 비동기 작업을 동시에 기다리는 예제입니다."""

    # 함수 안에 작은 async 함수를 정의할 수도 있습니다.
    # 이 함수는 실제로는 외부 API나 DB를 조회하는 함수라고 생각하면 됩니다.
    async def fetch_mock_data(name: str, seconds: int):
        # 외부 API 호출처럼 시간이 걸리는 작업을 흉내 냅니다.
        await asyncio.sleep(seconds)
        return {"name": name, "seconds": seconds}

    # gather는 여러 async 작업을 동시에 실행하고 모두 끝날 때까지 기다립니다.
    # 순서대로 기다리면 1 + 2 + 1 = 약 4초가 걸리지만,
    # 동시에 기다리면 가장 오래 걸리는 작업 기준으로 약 2초에 끝납니다.
    results = await asyncio.gather(
        fetch_mock_data("profile", 1),
        fetch_mock_data("history", 2),
        fetch_mock_data("logs", 1),
    )

    return {"data": results}
