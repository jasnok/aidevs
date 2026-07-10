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


plus, minus, multiply, divide = calculate(10, 2)

print("더하기:", plus)
print("빼기:", minus)
print("곱하기:", multiply)
print("나누기:", divide)


def get_min_max(numbers):
    smallest = min(numbers)
    largest = max(numbers)
    return smallest, largest


scores = [80, 95, 70, 88]
min_score, max_score = get_min_max(scores)

print("최저 점수:", min_score)
print("최고 점수:", max_score)
