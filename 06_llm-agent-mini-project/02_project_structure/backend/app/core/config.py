"""환경 변수 설정 파일입니다.

구현할 내용:
    1. python-dotenv로 .env 파일을 읽습니다.
    2. OPENAI_API_KEY, OPENAI_MODEL, USE_MOCK_DATA 값을 가져옵니다.
    3. API Key가 없을 때 Mock data로 동작할지 정책을 정합니다.
"""

import os
from dataclasses import dataclass

from dotenv import load_dotenv


load_dotenv()


@dataclass
class Settings:
    """프로젝트 전체에서 사용할 설정값입니다."""

    openai_api_key: str | None = os.getenv("OPENAI_API_KEY")
    openai_model: str = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
    use_mock_data: bool = os.getenv("USE_MOCK_DATA", "true").lower() == "true"


settings = Settings()
