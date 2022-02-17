#while문 활용 소인수 분해
a = int(input("? "))
x = 2
while a != 1:
      while a % x == 0:
             print(x)
             a = a / x
      x += 1
