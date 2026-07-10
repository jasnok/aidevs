"""중첩 자료구조와 API 응답 형태 예제입니다.

실제 API 응답은 list, dict가 여러 단계로 섞인 형태가 많습니다.

예를 들어 Supabase에서 대화 목록을 조회하거나,
LLM API에서 응답을 받을 때도 비슷한 구조를 만나게 됩니다.

이 예제에서는 API 응답처럼 생긴 dict를 만들고,
필요한 값을 하나씩 꺼내 봅니다.
"""

api_response = {
    "status": "success",
    "count": 2,
    "data": [
        {
            "id": 1,
            "user": {"name": "Jean", "role": "admin"},
            "message": "안녕하세요.",
            "tags": ["greeting", "korean"],
        },
        {
            "id": 2,
            "user": {"name": "Mina", "role": "member"},
            "message": "Python을 학습 중입니다.",
            "tags": ["python", "study"],
        },
    ],
}

print("응답 상태:", api_response["status"])
print("데이터 개수:", api_response["count"])

messages = api_response["data"]

print("\n[메시지 목록]")

for message in messages:
    message_id = message["id"]
    user_name = message["user"]["name"]
    user_role = message["user"]["role"]
    text = message["message"]
    tags = message["tags"]

    print("ID:", message_id)
    print("작성자:", user_name)
    print("역할:", user_role)
    print("내용:", text)
    print("태그:", ", ".join(tags))
    print("-" * 20)

print("중첩 자료구조에서는 바깥에서 안쪽으로 한 단계씩 접근합니다.")
