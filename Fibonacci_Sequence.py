num = int(input())


def fibonacci(n):
   if n<=1:
      return n	
   else:
      return (fibonacci(n-2) + fibonacci(n-1)) 


fibonacci(num)
for i in range(num):
   print(fibonacci(i))
