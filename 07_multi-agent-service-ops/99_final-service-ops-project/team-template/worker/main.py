r"""RUN GUIDE

Run from:
    C:\aidev\07_multi-agent-service-ops\99_final-service-ops-project\team-template\worker

Run command:
    python .\main.py

Purpose:
    Small example file for the 07 service-ops course.
"""

"""Auto Healing worker 샘플입니다."""

import time

import httpx


def main() -> None:
    """worker가 주기적으로 backend health를 확인하는 흐름을 흉내 냅니다."""

    print("worker started")
    for index in range(3):
        try:
            response = httpx.get("http://backend:8000/health", timeout=5)
            print(f"health check {index + 1}: {response.json()}")
        except httpx.HTTPError as exc:
            print(f"health check failed: {exc}")
        time.sleep(2)
    print("worker finished")


if __name__ == "__main__":
    main()
