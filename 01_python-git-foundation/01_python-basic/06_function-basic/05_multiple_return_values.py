"""여러 값을 반환하는 함수 예제입니다.

Python 함수는 여러 값을 한 번에 반환할 수 있습니다.
실제로는 tuple 형태로 반환되고, 이를 여러 변수에 나누어 받을 수 있습니다.
"""


def calculate(a, b):
    add_result = a + b
    subtract_result = a - b
    multiply_result = a * b
    divide_result = a / b

    return add_result, subtract_result, multiply_result, divide_result

result: tuple[float, float, float, float] = calculate(10.0, 2.0)
for value in result:
    print(value)

plus, minus, multiply, divide = calculate(10, 2)

print("더하기:", plus)
print("빼기:", minus)
print("곱하기:", multiply)
print("나누기:", divide)


def get_min_max(numbers: list[int]) -> tuple[int, int]:
    """리스트에서 최솟값과 최댓값을 반환하는 함수입니다."""
    smallest = min(numbers)
    largest = max(numbers)
    return smallest, largest


scores = [80, 95, 70, 88]
min_score, max_score = get_min_max(scores)

print("최저 점수:", min_score)
print("최고 점수:", max_score)

print("===" * 10)

# 숫자로 되어있는 List를 입력하면
# 최솟값, 최댓값, 합계, 평균을 반환하는 함수를 만들어보세요.
# dict 형태로 반환하는 함수를 구현해보세요.

def get_statistics(numbers: list[int]) -> dict[str, float]:
    """리스트에서 최솟값, 최댓값, 합계, 평균을 반환하는 함수입니다."""
    smallest = min(numbers)
    largest = max(numbers)
    total = sum(numbers)
    average = total / len(numbers)

    return {
        "min": smallest,
        "max": largest,
        "sum": total,
        "average": average
    }


scores = [80, 95, 70, 88]
stats = get_statistics(scores)

for key, value in stats.items():
    print(f"{key.capitalize()}: {value}")