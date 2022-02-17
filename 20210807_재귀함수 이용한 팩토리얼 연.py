#재귀함수 이용한 팩토리얼 연산
def fact(x):
      res = 1
      if x <= 1:
            return res
      return x*fact(x-1)

print(fact(7))
