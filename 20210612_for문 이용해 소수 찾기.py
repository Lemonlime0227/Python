#2 ~ 100까지 소수 찾기 프로그램
hasdiv=0 #true false boolean
for n in range(2,101,1):
      for div in range(2,n,1):
            if n % div == 0:
                  hasdiv = 1
                  break
      if hasdiv == 0:
            print(n, end = ' ')
      hasdiv = 0
