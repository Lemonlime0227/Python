#time모듈을 이용한 타자게임
import random as r
import time as t

w = ["cat", "dog", "fox", "monkey" , "mouse" , "panda" , "frog" , "snake" , "wolf"]
n = 1

print("[타자게임] 준비되면 엔터!")
input()

start = t.time()
q = r.choice(w)
while n <= 5:
      print("*문제", n)
      print(q)
      x = input()
      if x == q:
            print("통과!")
            n = n+1
            q = r.choice(w)
      else:
            print("오타! 다시 도전!")

end = t.time()
et = end - start
ea = format(et, ".2f")
print("타자 시간:" , ea)
