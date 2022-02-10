num=int(input("수를 입력하여 주세요:"))
#[//-몫만 출력] [**-제곱 출력] [%-나머지만 출력]
if num<=0:
    print("자연수가 아닙니다")
elif num % 2 == 0:
    print("짝수입니다")
elif num % 2 == 1:
    print("홀수입니다")
