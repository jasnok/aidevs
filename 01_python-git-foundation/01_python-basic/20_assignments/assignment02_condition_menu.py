# # Assignment 02 - Condition Menu

# 조건문을 사용해 메뉴 기반 프로그램을 만듭니다.

# ## 과제 파일

# ```text
# submissions/assignment02_condition_menu.py
# ```

# ## 요구사항

# ```text
# 1. 메뉴를 출력합니다.
# 2. 메뉴 번호를 입력받습니다.
# 3. 1번: 점수 등급 계산
# 4. 2번: 숫자 양수/0/음수 판별
# 5. 3번: 사용자 역할 안내
# 6. 그 외: 알 수 없는 메뉴 안내
# ```

# ## 세부 조건

# 점수 등급 계산:

# ```text
# 90 이상: A
# 80 이상: B
# 70 이상: C
# 그 외: D
# ```

# 사용자 역할 안내:

# ```text
# admin: 관리자입니다.
# member: 일반 사용자입니다.
# guest: 게스트입니다.
# 그 외: 알 수 없는 역할입니다.
# ```

# ## 권장 문법

# ```text
# if
# elif
# else
# match-case
# ```

# ## 확인 기준

# ```text
# 여러 조건이 올바른 순서로 검사되는가?
# 잘못된 메뉴 입력도 처리하는가?
# match-case 또는 if/elif/else 중 적절한 방식을 선택했는가?
# ```

print("start ...")

while True:
    print("Menu Start ")
    cmd = input("Input cmd..")
    print(f"입력하신 정보는 {cmd}")
    if (cmd == "1"):
        print("1번: 점수 등급 계산")
        score:int = int(input("점수를 입력하세요 : "))
        if(score>=90) :
            print("A")
        elif(score<90 and score>=80) :
            print("B")
        elif(score<80 and score>=70) :
            print("C")
        else :
            print("D")
    elif (cmd == "2"):
        print("2번: 숫자 양수/0/음수 판별")
        number:int = int(input(" 숫자를 입력하세요 : "))
        if(number>0) :
            print("양수")
        elif(number==0) :
            print("0")
        else:
            print("음수")
    elif (cmd == "3"):
        print("3번: 사용자 역할 안내")
        role:str = input("사용자의 역할을 입력하세요 : ")
        if(role == "admin") :
            print("관리자입니다.")
        elif(role == "member") :
            print("일반 사용자입니다.")
        elif(role == "guest") :
            print("게스트입니다.")
        else :
            print("알 수 없는 역할입니다.")   
    elif (cmd == "q"):
        print("Bye ...")
        break
    else: 
        print("잘못된 메뉴를 선택하셨습니다.")
print("end ....")