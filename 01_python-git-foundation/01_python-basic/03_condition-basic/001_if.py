import sys

print("start ....")

input_data = input("무엇을 넣었습니까?")

if(input_data != "카드"):
    print("카드가 아닙니다")
    sys.exit()

print("카드입니다")