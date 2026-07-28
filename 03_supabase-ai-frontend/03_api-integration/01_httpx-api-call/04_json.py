import httpx  # 외부 API에 HTTP 요청을 보내기 위해 httpx를 가져옵니다.

API_URL = "https://jsonplaceholder.typicode.com/posts"  # 게시글 목록 API 주소입니다.

response = httpx.get(
    API_URL,
    timeout=5.0
)  # GET 요청을 보내고 응답 객체를 response 변수에 저장합니다.

print("status code:", response.status_code)  # HTTP 요청의 상태 코드를 출력합니다.
print("json:", response.json())  # 서버가 보내준 전체 JSON 데이터를 출력합니다.

# JSON 데이터를 파이썬의 list 또는 dict 형태로 변환합니다.
result = response.json()

print(type(response))  # httpx 응답 객체의 자료형을 확인합니다.
print(type(result))  # 변환된 결과의 자료형을 확인합니다.

# result에는 여러 개의 게시글이 리스트 형태로 들어 있습니다.
for post in result:
    print("userId:", post["userId"])
    print("id:", post["id"])
    print("title:", post["title"])
    print("body:", post["body"])
    print("-" * 50)