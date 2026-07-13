numbers:list[int] = [1, 2, 3, 4, 5]

# 1. 출력
print("numbers:", numbers)

# 2. 마지막에 6을 추가
numbers.append(6)
print("6을 추가한 후:", numbers)

# 3. 전체 합과 평균을 출력 단, 짝수만 합과 평균을 구합니다..
total = 0
count = 0
for n in numbers:
    if n % 2 == 0:
        total += n
        count += 1

if count > 0:
    average = total / count
else:
    average = 0
    
print("전체 합:", total)
print("평균:", average)