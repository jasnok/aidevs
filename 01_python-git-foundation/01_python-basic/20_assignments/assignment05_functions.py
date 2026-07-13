# # Assignment 05 - Functions

# 기존 코드를 함수로 분리하는 과제입니다.

# ## 과제 파일

# ```text
# submissions/assignment05_functions.py
# ```

# ## 요구사항

# 아래 함수를 모두 만듭니다.

# ```text
# get_grade(score)
# is_passed(score)
# calculate_average(scores)
# filter_passed_students(students)
# print_student(student)
# ```

# ## 함수 설명

# ```text
# get_grade(score): 점수를 받아 A/B/C/D를 반환합니다.
# is_passed(score): 60점 이상이면 True를 반환합니다.
# calculate_average(scores): 점수 list를 받아 평균을 반환합니다.
# filter_passed_students(students): 통과한 학생 dict만 모아 list로 반환합니다.
# print_student(student): 학생 dict 하나를 보기 좋게 출력합니다.
# ```

# ## 데이터 예시

# ```python
# students = [
#     {"name": "Jean", "score": 95},
#     {"name": "Mina", "score": 82},
#     {"name": "Jun", "score": 58},
# ]
# ```

# ## 확인 기준

# ```text
# 함수가 값을 return하는가?
# 함수 이름이 역할을 잘 설명하는가?
# 같은 함수를 여러 데이터에 재사용했는가?
# ```

students = [
    {"name": "Jean", "score": 95},
    {"name": "Mina", "score": 82},
    {"name": "Jun", "score": 58},
    {"name": "Tom", "score": 70},
    {"name": "Jerry", "score": 45},
    {"name": "Alice", "score": 88},
]

# 1. 학생들의 평균점수를 출력한다.
# calculate_average(students:list) -> float:
def calculate_average(students):
    total_score = sum(student['score'] for student in students)
    average = total_score / len(students)
    return average

print("학생들의 평균점수:", calculate_average(students))

# 2. 학생의 학점(90=A,80=B,70=C,60=D)과 학생의 점수와 패스여부(60점 이상=pass, 60점 미만=fail)를 출력한다.
# print_student_status(student:dict) -> tuple(str, bool):
def print_student_status(student:dict):
    score = student['score']
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'F'
    
    passed = score >= 60
    return (grade, passed)

print("\n학생들의 학점과 점수와 패스여부:") #점수순으로 내림차순
students_sorted = sorted(students, key=lambda x: x['score'], reverse=True)
for student in students_sorted:
    grade, passed = print_student_status(student)
    print(f"{student['name']} - 점수: {student['score']}, 학점: {grade}, 패스여부: {'pass' if passed else 'fail'}")


# 3. 모든 학생의 평균점수보다 낮은 학생들을 조회하여 출력한다.
# filter_failed_students(students:list, average:float) -> tuple:
def filter_failed_students(students, average):
    failed_students = [student for student in students if student['score'] < average]
    return failed_students

print("\n평균점수보다 낮은 학생들:") #평균점수를 출력하고 평균점수보다 낮은 학생들을 점수순으로 내림차순해서 출력하시오.
average = calculate_average(students)
print(f"평균점수: {average:.2f}")
failed_students = filter_failed_students(students, average)
failed_students_sorted = sorted(failed_students, key=lambda x: x['score'], reverse=True)
for student in failed_students_sorted:
    print(f"{student['name']} - 점수: {student['score']}")

print("\n프로그램 종료")