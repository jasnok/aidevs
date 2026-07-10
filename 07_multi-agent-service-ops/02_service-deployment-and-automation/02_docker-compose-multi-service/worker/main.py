r"""RUN GUIDE

Run from:
    C:\aidev\07_multi-agent-service-ops\02_service-deployment-and-automation\02_docker-compose-multi-service\worker

Run command:
    python .\main.py

Purpose:
    Small example file for the 07 service-ops course.
"""

"""Docker Compose worker 서비스 예제입니다."""

import time


def main() -> None:
    """백그라운드 작업자가 시작되었음을 출력합니다."""

    print("worker started")
    print("Auto Healing 또는 Agent 작업 실행기가 이 위치에 들어갑니다.")
    time.sleep(2)
    print("worker finished sample job")


if __name__ == "__main__":
    main()
