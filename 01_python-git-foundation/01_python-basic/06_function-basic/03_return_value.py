"""반환값(return) 기초 예제입니다.

return은 함수의 결과를 함수 밖으로 돌려주는 문법입니다.

print는 화면에 보여 주는 것이고,
return은 값을 다음 계산이나 다른 함수에서 다시 사용할 수 있게 해 줍니다.
"""


def add(a: float, b: float)-> float:
    result = a + b
    return result

def divide(a: float, b: float) -> float:
    if b == 0:
        return None  # 0으로 나누는 경우 None을 반환하도록 처리
    result = a / b
    return result

divide_result = divide(10, 2)
print("나누기 결과:", divide_result)

divide_result_zero = divide(10, 0)
print("나누기 결과:", divide_result_zero)

def make_greeting(name: str ) -> str:
    message = f"{name}님, 안녕하세요."
    return message


sum_result = add(3, 5)
print("더하기 결과:", sum_result)

# return으로 받은 값을 다시 계산에 사용할 수 있습니다.
double_result = sum_result * 2
print("두 배 결과:", double_result)

greeting = make_greeting("Jean")
print(greeting)

# return을 만나면 함수는 즉시 종료됩니다.
def check_number(number):
    if number < 0:
        return "음수입니다."
    if number == 0:
        return "0입니다."
    if  number > 0:
        return "양수입니다."

    return None  # 모든 조건에 해당하지 않는 경우 None을 반환


print(check_number(-3))
print(check_number(10))
