import sys

print("start ....")

input_data = "카드4"

if(input_data != "카드1" and input_data != "카드2" and input_data != "카드3"):
    print("카드가 아닙니다")
    sys.exit()

if(input_data == "카드1"):
    print("카드 1 업무 진행")
elif(input_data == "카드2"):
    print("카드 2 업무 진행")
elif(input_data == "카드3"):
    print("카드 3 업무 진행")
else:
    print("카드가 정상이 아닙니다.")