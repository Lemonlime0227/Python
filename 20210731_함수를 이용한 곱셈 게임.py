import random as r
def question():
      a = r.randint(1,10)
      b = r.randint(1,10)
      c = r.randint(1,3)
      a1 = str(a)
      if c == 1:
            a1 += "+"
      elif c == 2:
            a1 += "-"
      elif c == 3:
            a1 += "*"
      a1 += str(b)
      return a1

O = 0
X = 0
for x in range(5):
      q = question()
      print(q)
      ans = int(input("="))
      if ans == eval(q):                  #문자열 반환 eval() 계산
            print("정답!")
            O += 1
      else:
            print("오답!")
            X += 1
print("정답 수:", O,"오답 수:", X)
if X == 0:
      print("당신은 천재입니다!")
else:
      print("아쉽지만 다음에는 5개를 다 맞춰보세요")
            
