#퀵 정렬
d = [8,5,6,4,1,3,9,10,7,2]
for x in range(0, len(d)):
      mini = 100
      for y in range(x, len(d)):
            if mini > d[y]:
                  mini = d[y]
                  index = y
      temp = d[x]
      d[x] = d[index]
      d[index] = temp
      print(d)
            
