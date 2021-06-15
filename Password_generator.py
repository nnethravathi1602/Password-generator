import random
import string

upper=string.ascii_uppercase
lower=string.ascii_uppercase
numbers=random.randrange(1,10)
symbols=string.punctuation

all=upper+lower+str(numbers)+symbols
length=16

password="".join(random.sample(all,length))
print("your password : ",password)
