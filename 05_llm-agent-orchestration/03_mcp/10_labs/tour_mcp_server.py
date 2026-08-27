"""여행지 명소 정보를 조회하는 교육용 stdio MCP Server입니다.
    Arg 지명은 부산, 서울 이고 return 값은 관광정보 입니다.
    관광정보는 관광지명, 주소, 운영시간, 입장료, 설명으로 구성되어 있습니다.
    관광지명은 부산의 경우 해운대, 광안리, 자갈치, 서울의 경우 경복궁, 남산타워, 명동으로 구성되어 있습니다.
    운영시간은 오전 9시 ~ 오후 6시, 입장료는 무료입니다.
"""

from typing import Literal

from mcp.server.fastmcp import FastMCP

mcp = FastMCP(
    "tour",
    instructions="여행지 명소 정보를 조회합니다.",
)

ATTRACTIONS = [
    {
        "attraction_id": "attraction-busan-001",
        "name": "해운대",
        "city": "부산",
        "address": "부산 해운대구 해운대해변로 264",
        "hours": "오전 9시 ~ 오후 6시",
        "entry_fee": "무료",
        "description": "부산의 대표적인 해수욕장으로, 아름다운 해변과 다양한 해양 스포츠를 즐길 수 있습니다.",
    },
    {
        "attraction_id": "attraction-busan-002",
        "name": "광안리",
        "city": "부산",
        "address": "부산 수영구 광안해변로 219",
        "hours": "오전 9시 ~ 오후 6시",
        "entry_fee": "무료",
        "description": "광안대교가 보이는 해변으로, 야경이 아름답고 다양한 카페와 음식점이 즐비합니다.",
    },
    {
        "attraction_id": "attraction-busan-003",
        "name": "자갈치",
        "city": "부산",
        "address": "부산 중구 자갈치해안로 52",
        "hours": "오전 9시 ~ 오후 6시",
        "entry_fee": "무료",
        "description": "부산의 대표적인 수산시장으로, 신선한 해산물을 맛볼 수 있는 곳입니다.",
    },
    {
        "attraction_id": "attraction-seoul-001",
        "name": "경복궁",
        "city": "서울",
        "address": "서울 종로구 사직로 161",
        "hours": "오전 9시 ~ 오후 6시",
        "entry_fee": "무료",
        "description": "조선 시대의 대표적인 궁궐로, 한국 전통 건축과 역사를 체험할 수 있습니다.",
    },
    {
        "attraction_id": "attraction-seoul-002",
        "name": "남산타워",
        "city": "서울",
        "address": "서울 용산구 남산공원길 105",
        "hours": "오전 9시 ~ 오후 6시",
        "entry_fee": "무료",
        "description": "서울의 랜드마크 중 하나로, 전망대에서 서울 시내를 한눈에 볼 수 있습니다.",
    },
]

@mcp.tool()
def get_attractions(city: Literal["부산", "서울"]) -> dict:
    """도시의 관광지 정보를 조회합니다."""
    matches = [
        attraction for attraction in ATTRACTIONS
        if attraction["city"] == city
    ]
    return {"items": matches, "source": "lab-tour-attractions"}

if __name__ == "__main__":
    mcp.run(transport="stdio")