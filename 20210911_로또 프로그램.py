#로또 프로그램
import random
weeklotto= [0,0,0,0,0,0]
resl = []
game = int(input("게임 수 "))
for x in range(0,6):
          weeklotto[x] = random.randint(1,45)
          for y in range(0,x):
                    while weeklotto[x] == weeklotto[y]:
                              weeklotto[x] = random.randint(1,45)
weeklotto.sort()
print(weeklotto)
print()
for x in range(0,game):
          lotto = random.sample(range(1,46),6)
          lotto.sort()
          print(lotto)
          res = 0
          for z in range(0,6):
                    for a in range(0,6):
                              if lotto[z] == weeklotto[a]:
                                        res += 1
          resl.append(res)
for x in range(0,game):
          print(x+1,"번,", resl[x],"개 일치")
