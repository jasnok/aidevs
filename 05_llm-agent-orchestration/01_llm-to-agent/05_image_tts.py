# 05_image_tts.py
# 이미지를 올리면 해당 이미지를 분석한 내용을 음성 파일로 만든다.

import base64
import mimetypes
import os
from pathlib import Path
import sys

from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel


class FootballPlayerAnalysis(BaseModel):
    player_name_text: str | None = None
    jersey_number: str | None = None
    uniform_description: str | None = None
    team_guess: str | None = None
    spoken_summary: str | None = None


load_dotenv()

image_path = Path(sys.argv[1])
content_type = mimetypes.guess_type(image_path.name)[0] or "image/jpeg"

encoded = base64.b64encode(image_path.read_bytes()).decode("ascii")

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])


# 1. 축구선수 이미지 분석
response = client.responses.parse(
    model=os.getenv("OPENAI_VISION_MODEL", "gpt-4.1-mini"),
    instructions=(
        "축구선수 이미지를 한국어로 분석하세요. "
        "선수의 얼굴을 보고 신원을 추측하지 말고, "
        "유니폼에 실제로 보이는 이름과 등번호를 읽으세요. "
        "유니폼의 색상, 로고, 스폰서, 디자인을 바탕으로 팀 이름을 추정하세요. "
        "팀 이름이 확실하지 않으면 추정값으로 처리하세요. "
        "spoken_summary는 반드시 "
        "'[팀 이름]의 [등번호]번 선수 [유니폼에 적힌 이름]로 보입니다.' "
        "형식의 한 문장으로 작성하세요."
    ),
    input=[
        {
            "role": "user",
            "content": [
                {
                    "type": "input_text",
                    "text": (
                        "유니폼에 보이는 선수 이름, 등번호, "
                        "유니폼 특징을 분석하고 팀 이름도 추정해 주세요."
                    ),
                },
                {
                    "type": "input_image",
                    "image_url": f"data:{content_type};base64,{encoded}",
                },
            ],
        }
    ],
    text_format=FootballPlayerAnalysis,
)

analysis = response.output_parsed

print(analysis.model_dump_json(indent=2))


# 2. 이미지 분석 결과를 음성으로 변환
spoken_text = analysis.spoken_summary

output_path = Path(__file__).with_name("player-guide.mp3")

with client.audio.speech.with_streaming_response.create(
    model=os.getenv("OPENAI_TTS_MODEL", "gpt-4o-mini-tts"),
    voice=os.getenv("OPENAI_TTS_VOICE", "coral"),
    input=spoken_text,
    instructions="한국어로 또렷하고 차분한 축구 중계 해설처럼 말하세요.",
) as response:
    response.stream_to_file(output_path)

print("AI 합성 음성을 생성했습니다:", output_path)