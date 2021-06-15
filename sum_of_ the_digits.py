n = int(input())

length = 0

while n > 0 :
   k=n%10
   n//=10
   length += k

print(length)
