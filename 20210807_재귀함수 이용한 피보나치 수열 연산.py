#재귀함수 이용한 피보나치 수열 연산 
def fibo(n):
      if n <= 1:
            return n
      return fibo(n-2) + fibo(n-1)

print(fibo(7))

