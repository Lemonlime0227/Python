#math 모듈 활용하여 이차방정식 풀기
import math
import sys
print("ax^2 + bx + c = 0")
a = float(input("a? "))
b = float(input("b? "))
c = float(input("c? "))

if a == 0:
      print("a = 0이므로 이차방정식이 아닙니다")
      sys.exit()

D = b ** 2 - 4 * a * c

if D > 0:
      x1 = (-b + math.sqrt(D))/(2*a)
      x2 = (-b - math.sqrt(D))/(2*a)
      print("2개의 해:" , x1, x2)
elif D == 0:
      x = -b / (2*a)
      print("한개의 해:", x)
elif D < 0:
      print("해가 없습니다.")
