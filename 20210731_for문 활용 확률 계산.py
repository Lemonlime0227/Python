#확률 계산
import random

seq = int(input("원하는 수를 입력하세요:"))
res = 0

for i in range(seq):
      if random.randint(1, 6) == 2:
            res += 1
print((res / seq) * 100 , "%")
