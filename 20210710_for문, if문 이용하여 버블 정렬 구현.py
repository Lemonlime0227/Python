#버블 정렬
a = [6, 3, 8 ,9 , 1, 10, 7, 5, 4, 2]
for y in range(0, 9):
      for x in range(0, 9-y):
            b = a[x+1]
            if a[x] > a[x+1]:
                  a[x+1] = a[x]
                  a[x] = b
      print(a)
print(a)
