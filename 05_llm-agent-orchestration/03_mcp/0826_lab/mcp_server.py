"""stdio로 실행되는 교육용 귀가도우미 MCP Server입니다."""

from datetime import datetime
import sys
from typing import Literal

from mcp.server.fastmcp import FastMCP


mcp = FastMCP(
    "return-home-tools",
    instructions=(
        "술집 이용 후 안전한 귀가를 위한 지하철, 버스, 택시, "
        "대리기사 정보를 제공합니다. 교통 정보는 Mock Data입니다."
    ),
)


TRANSPORT_DATA = {
    "서울대입구역": {
        "subway": {
            "route": "지하철 2호선 이용",
            "last_departure": "23:45",
            "duration_minutes": 35,
            "estimated_cost_won": 1_500,
        },
        "bus": {
            "route": "간선버스 501번 이용",
            "last_departure": "23:30",
            "duration_minutes": 45,
            "estimated_cost_won": 1_500,
        },
        "taxi": {"duration_minutes": 25, "estimated_cost_won": 18_000},
        "designated_driver": {
            "duration_minutes": 30,
            "estimated_cost_won": 25_000,
        },
    },
    "강남역": {
        "subway": {
            "route": "지하철 2호선 이용",
            "last_departure": "00:10",
            "duration_minutes": 20,
            "estimated_cost_won": 1_500,
        },
        "bus": {
            "route": "간선버스 420번 이용",
            "last_departure": "23:50",
            "duration_minutes": 30,
            "estimated_cost_won": 1_500,
        },
        "taxi": {"duration_minutes": 15, "estimated_cost_won": 12_000},
        "designated_driver": {
            "duration_minutes": 20,
            "estimated_cost_won": 20_000,
        },
    },
    "홍대입구역": {
        "subway": {
            "route": "지하철 환승 1회",
            "last_departure": "23:35",
            "duration_minutes": 40,
            "estimated_cost_won": 1_600,
        },
        "bus": {
            "route": "간선버스 271번 이용",
            "last_departure": "23:20",
            "duration_minutes": 50,
            "estimated_cost_won": 1_500,
        },
        "taxi": {"duration_minutes": 30, "estimated_cost_won": 22_000},
        "designated_driver": {
            "duration_minutes": 35,
            "estimated_cost_won": 30_000,
        },
    },
}


def _minutes(time_text: str) -> int:
    """HH:MM 형식의 시각을 하루의 누적 분으로 변환합니다."""
    try:
        parsed = datetime.strptime(time_text, "%H:%M")
    except ValueError as exc:
        raise ValueError("departure_time은 HH:MM 형식이어야 합니다.") from exc
    return parsed.hour * 60 + parsed.minute


def _is_available(departure_time: str, last_departure: str) -> bool:
    """자정을 넘는 막차까지 고려하여 이용 가능 여부를 반환합니다."""
    departure_minutes = _minutes(departure_time)
    last_departure_minutes = _minutes(last_departure)
    if last_departure_minutes < 3 * 60 and departure_minutes >= 18 * 60:
        last_departure_minutes += 24 * 60
    return departure_minutes <= last_departure_minutes


@mcp.tool()
def get_return_transport_options(
    destination: Literal["서울대입구역", "강남역", "홍대입구역"],
    departure_time: str = "",
) -> dict:
    """목적지와 출발 시각에 맞는 지하철, 버스, 택시, 대리기사 정보를 조회합니다."""
    normalized_destination = destination.strip()
    if normalized_destination not in TRANSPORT_DATA:
        raise ValueError("지원하는 목적지는 서울대입구역, 강남역, 홍대입구역입니다.")

    normalized_time = departure_time.strip() or datetime.now().strftime("%H:%M")
    _minutes(normalized_time)
    data = TRANSPORT_DATA[normalized_destination]

    subway = data["subway"]
    bus = data["bus"]
    return {
        "origin": "현재 술집",
        "destination": normalized_destination,
        "departure_time": normalized_time,
        "subway": {
            "available": _is_available(normalized_time, subway["last_departure"]),
            **subway,
        },
        "bus": {
            "available": _is_available(normalized_time, bus["last_departure"]),
            **bus,
        },
        "taxi": {"available": True, **data["taxi"]},
        "designated_driver": {
            "available": True,
            "vehicle_required": True,
            **data["designated_driver"],
        },
        "is_mock_data": True,
        "notice": "교육용 Mock Data이므로 실제 출발 전 교통 정보를 확인하세요.",
    }


if __name__ == "__main__":
    print("귀가도우미 MCP Server를 stdio로 실행합니다.", file=sys.stderr)
    mcp.run(transport="stdio")
