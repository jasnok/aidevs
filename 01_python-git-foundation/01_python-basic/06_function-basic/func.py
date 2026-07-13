def add_numbers(a: int, b: int) -> int:
    """두 수를 더하는 함수입니다."""
    return a + b

def calculate_average(numbers: list[int]) -> float:
    """리스트의 평균을 계산하는 함수입니다."""
    total = sum(numbers)
    average = total / len(numbers)
    return average

number1 = 10
number2 = 20
total = add_numbers(number1, number2)
avg = total / 2
print("합계:", total)
print("평균:", avg)

number3 = 30
number4 = 40
total2 = add_numbers(number3, number4)
avg2 = total2 / 2
print("합계:", total2)
print("평균:", avg2)

# 각 데이터의 평균보다 큰 수를 리턴하는 함수를 만들어보세요.
def filter_greater_than_average(numbers: list[int]) -> tuple[int]:
    """리스트에서 평균보다 큰 수를 반환하는 함수입니다."""
    average = calculate_average(numbers)
    return tuple(num for num in numbers if num > average)

datas1 = [10, 20, 30, 40]
filtered1 = filter_greater_than_average(datas1)
print("평균 :", sum(datas1) / len(datas1))
print("평균보다 큰 수:", filtered1)

datas2 = [5, 15, 25, 35]
filtered2 = filter_greater_than_average(datas2)
print("평균 :", sum(datas2) / len(datas2))
print("평균보다 큰 수:", filtered2)
