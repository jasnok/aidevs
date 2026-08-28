"""기상청 API를 호출하고 날씨 응답을 정리합니다."""

import logging
import os
from datetime import datetime, timedelta
from urllib.parse import unquote
from zoneinfo import ZoneInfo

import httpx
from dotenv import load_dotenv


load_dotenv()

# httpx의 INFO 로그에는 query string과 API Key가 포함될 수 있습니다.
logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("httpcore").setLevel(logging.WARNING)

# 공공데이터포털의 일반 인증키는 이미 URL 인코딩되어 있을 수 있습니다.
# 한 번 디코딩한 값을 httpx에 전달하면 요청할 때 정상적으로 한 번 인코딩됩니다.
KMA_API_KEY = unquote(os.getenv("KMA_API_KEY", ""))
KMA_API_URL = "https://apis.data.go.kr/1360000/VilageFcstInfoService_2.0"
KST = ZoneInfo("Asia/Seoul")

REGIONS = {
    "서울": {"nx": 60, "ny": 127},
    "부산": {"nx": 98, "ny": 76},
    "인천": {"nx": 55, "ny": 124},
    "대전": {"nx": 67, "ny": 100},
    "대구": {"nx": 89, "ny": 90},
    "광주": {"nx": 58, "ny": 74},
    "울산": {"nx": 102, "ny": 84},
    "세종": {"nx": 66, "ny": 103},
}

SKY_CODES = {
    "1": "맑음",
    "3": "구름많음",
    "4": "흐림",
}

PTY_CODES = {
    "0": "강수 없음",
    "1": "비",
    "2": "비/눈",
    "3": "눈",
    "4": "소나기",
    "5": "빗방울",
    "6": "빗방울/눈날림",
    "7": "눈날림",
}


def get_latest_observation_time(now: datetime) -> datetime:
    """초단기실황 API에서 조회 가능한 최근 발표시각을 구합니다."""
    if now.minute < 10:
        now = now - timedelta(hours=1)
    return now.replace(minute=0, second=0, microsecond=0)


def get_latest_forecast_time(now: datetime) -> datetime:
    """초단기예보 API에서 조회 가능한 최근 발표시각을 구합니다."""
    if now.minute < 45:
        now = now - timedelta(hours=1)
    return now.replace(minute=30, second=0, microsecond=0)


def request_kma(endpoint: str, base_time: datetime, nx: int, ny: int) -> list:
    """기상청 API를 호출하고 item 목록을 반환합니다."""
    if not KMA_API_KEY:
        raise ValueError("KMA_API_KEY가 없습니다. .env 파일을 확인해 주세요.")

    params = {
        "serviceKey": KMA_API_KEY,
        "pageNo": 1,
        "numOfRows": 1000,
        "dataType": "JSON",
        "base_date": base_time.strftime("%Y%m%d"),
        "base_time": base_time.strftime("%H%M"),
        "nx": nx,
        "ny": ny,
    }

    try:
        response = httpx.get(
            f"{KMA_API_URL}/{endpoint}",
            params=params,
            timeout=10.0,
        )
        response.raise_for_status()
        data = response.json()
    except httpx.RequestError as error:
        raise RuntimeError("기상청 API 네트워크 연결에 실패했습니다.") from None
    except httpx.HTTPStatusError as error:
        raise RuntimeError(
            f"기상청 API HTTP 오류: {error.response.status_code}"
        ) from None
    except ValueError as error:
        raise RuntimeError("기상청 API가 JSON 형식으로 응답하지 않았습니다.") from None

    header = data.get("response", {}).get("header", {})
    result_code = str(header.get("resultCode", ""))
    if result_code not in {"0", "00"}:
        result_message = header.get("resultMsg", "알 수 없는 오류")
        raise RuntimeError(f"기상청 API 오류: {result_code} {result_message}")

    items = data.get("response", {}).get("body", {}).get("items", {}).get("item", [])
    if not items:
        raise RuntimeError("기상청 API 응답에 날씨 데이터가 없습니다.")
    return items


def get_nearest_sky(items: list, now: datetime) -> tuple[str, str]:
    """현재 시각과 가장 가까운 SKY 예보값과 예보시각을 반환합니다."""
    sky_items = []
    for item in items:
        if item.get("category") != "SKY":
            continue
        forecast_time = datetime.strptime(
            item["fcstDate"] + item["fcstTime"],
            "%Y%m%d%H%M",
        ).replace(tzinfo=KST)
        sky_items.append((forecast_time, str(item["fcstValue"])))

    if not sky_items:
        raise RuntimeError("초단기예보 응답에 SKY 데이터가 없습니다.")

    forecast_time, sky_code = min(
        sky_items,
        key=lambda value: abs(value[0] - now),
    )
    sky = SKY_CODES.get(sky_code, f"알 수 없는 하늘상태({sky_code})")
    return sky, forecast_time.strftime("%Y-%m-%d %H:%M")


def get_current_weather(location: str, now: datetime | None = None) -> dict:
    """지역의 실황과 가장 가까운 SKY 예보를 합쳐 반환합니다."""
    normalized_location = location.strip()
    if normalized_location not in REGIONS:
        supported = ", ".join(REGIONS)
        raise ValueError(
            f"지원하지 않는 지역입니다: {normalized_location}. "
            f"지원 지역: {supported}"
        )

    current_time = now or datetime.now(KST)
    region = REGIONS[normalized_location]

    observation_time = get_latest_observation_time(current_time)
    forecast_time = get_latest_forecast_time(current_time)

    observation_items = request_kma(
        "getUltraSrtNcst",
        observation_time,
        region["nx"],
        region["ny"],
    )
    forecast_items = request_kma(
        "getUltraSrtFcst",
        forecast_time,
        region["nx"],
        region["ny"],
    )

    observations = {}
    for item in observation_items:
        observations[item["category"]] = item["obsrValue"]

    sky, sky_forecast_at = get_nearest_sky(forecast_items, current_time)
    precipitation_type = PTY_CODES.get(
        str(observations.get("PTY", "")),
        "알 수 없음",
    )
    weather = precipitation_type if precipitation_type != "강수 없음" else sky

    return {
        "location": normalized_location,
        "observed_at": observation_time.strftime("%Y-%m-%d %H:%M"),
        "sky_forecast_at": sky_forecast_at,
        "temperature_c": observations.get("T1H"),
        "humidity_percent": observations.get("REH"),
        "precipitation_1h_mm": observations.get("RN1"),
        "precipitation_type": precipitation_type,
        "sky": sky,
        "weather": weather,
        "wind_speed_mps": observations.get("WSD"),
        "data_note": "기온·습도·강수·바람은 실황, 하늘상태는 가장 가까운 초단기예보입니다.",
        "source": "기상청 단기예보 조회서비스",
    }
