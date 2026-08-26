"""stdio로 실행되는 교육용 귀가도우미 MCP Server입니다."""

from datetime import datetime
import sys
from typing import Literal

from mcp.server.fastmcp import FastMCP


mcp = FastMCP(
    "return-home-tools",
    instructions=(
        "술집 이용 후 안전한 귀가를 위한 교육용 교통 정보와 "
        "음주 후 운전 안전 안내를 제공합니다. 교통 정보는 Mock Data입니다."
    ),
)


TRANSPORT_DATA = {
    "서울대입구역": {
        "route": "지하철 2호선 이용",
        "last_departure": "23:45",
        "duration_minutes": 35,
        "public_transport_cost_won": 1_500,
        "taxi_duration_minutes": 25,
        "taxi_cost_won": 18_000,
    },
    "강남역": {
        "route": "지하철 2호선 이용",
        "last_departure": "00:10",
        "duration_minutes": 20,
        "public_transport_cost_won": 1_500,
        "taxi_duration_minutes": 15,
        "taxi_cost_won": 12_000,
    },
    "홍대입구역": {
        "route": "지하철 환승 1회",
        "last_departure": "23:35",
        "duration_minutes": 40,
        "public_transport_cost_won": 1_600,
        "taxi_duration_minutes": 30,
        "taxi_cost_won": 22_000,
    },
}


def _minutes(time_text: str) -> int:
    """HH:MM 형식의 시각을 하루의 누적 분으로 변환합니다."""
    try:
        parsed = datetime.strptime(time_text, "%H:%M")
    except ValueError as exc:
        raise ValueError("departure_time은 HH:MM 형식이어야 합니다.") from exc
    return parsed.hour * 60 + parsed.minute


@mcp.tool()
def get_return_transport_options(
    destination: Literal["서울대입구역", "강남역", "홍대입구역"],
    departure_time: str = "",
) -> dict:
    """목적지와 출발 시각을 기준으로 Mock 대중교통 및 택시 정보를 조회합니다."""
    normalized_destination = destination.strip()
    if normalized_destination not in TRANSPORT_DATA:
        raise ValueError("지원하는 목적지는 서울대입구역, 강남역, 홍대입구역입니다.")

    normalized_time = departure_time.strip() or datetime.now().strftime("%H:%M")
    departure_minutes = _minutes(normalized_time)
    data = TRANSPORT_DATA[normalized_destination]
    last_departure_minutes = _minutes(data["last_departure"])
    if last_departure_minutes < 3 * 60 and departure_minutes >= 18 * 60:
        last_departure_minutes += 24 * 60

    return {
        "origin": "현재 술집",
        "destination": normalized_destination,
        "departure_time": normalized_time,
        "public_transport": {
            "available": departure_minutes <= last_departure_minutes,
            "route": data["route"],
            "last_departure": data["last_departure"],
            "duration_minutes": data["duration_minutes"],
            "estimated_cost_won": data["public_transport_cost_won"],
        },
        "taxi": {
            "available": True,
            "duration_minutes": data["taxi_duration_minutes"],
            "estimated_cost_won": data["taxi_cost_won"],
        },
        "is_mock_data": True,
        "notice": "교육용 Mock Data이므로 실제 출발 전 교통 정보를 확인하세요.",
    }


@mcp.tool()
def get_safe_driving_guidance(
    drinking_status: Literal["마심", "마시지 않음", "알 수 없음"],
) -> dict:
    """음주 상태에 따라 직접 운전 여부와 안전한 귀가 대안을 안내합니다."""
    if drinking_status == "마심":
        return {
            "drinking_status": drinking_status,
            "should_drive": False,
            "message": "술을 마셨다면 직접 운전하지 마세요.",
            "alternatives": ["대중교통", "택시", "대리운전", "보호자 도움"],
            "notice": "혈중알코올농도나 법적 운전 가능 여부를 판정하지 않습니다.",
        }
    if drinking_status == "알 수 없음":
        return {
            "drinking_status": drinking_status,
            "should_drive": False,
            "message": "음주 여부가 확실하지 않다면 직접 운전하지 않는 것이 안전합니다.",
            "alternatives": ["대중교통", "택시", "대리운전", "보호자 도움"],
            "notice": "혈중알코올농도나 법적 운전 가능 여부를 판정하지 않습니다.",
        }
    return {
        "drinking_status": drinking_status,
        "should_drive": None,
        "message": "이 Tool은 운전 능력이나 법적 운전 가능 여부를 판정하지 않습니다.",
        "alternatives": ["피곤하거나 몸 상태가 좋지 않으면 대중교통 또는 택시 이용"],
        "notice": "안전을 우선하고 실제 몸 상태와 교통 상황을 확인하세요.",
    }


if __name__ == "__main__":
    print("귀가도우미 MCP Server를 stdio로 실행합니다.", file=sys.stderr)
    mcp.run(transport="stdio")
