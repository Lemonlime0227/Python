#try except 구문을 이용한 숫자맞추기
import random
number = random.randint(1,999)

while True:
          try:
                    guess = int(input("숫자를 입력하세요 :"))
                    if guess == number:
                              print("정답입니다")
                              break
                    elif guess > number:
                              print("더 작은 수 입니다")
                    else:
                              print("더 큰 수 입니다")
          except:
                    print("1~999 중의 숫자를 입력하세요")
