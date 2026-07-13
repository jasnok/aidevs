student: list[dict[str, object]] = [
    {
        "name": "Jean",
        "score": 95
    },
    {
        "name": "John",
        "score": 85
    },
    {
        "name": "Jane",
        "score": 90
    }
]

# 학생들 정보를 출력합니다. 
# for 반복문을 사용하여 학생들의 이름과 점수를 출력하시오.

print("학생 정보:")
for student_info in student:
    print("이름:", student_info["name"], ", 점수:", student_info["score"])

# 학생들 성적의 합과 평균을 출력하시오.
total_score = sum(student_info["score"] for student_info in student)
average_score = total_score / len(student)

print(f"성적 합: {total_score}")
print(f"성적 평균: {average_score}")
