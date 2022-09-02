#pass random value for prime number
import random as prabhat
a = [0,1,2,3,4,5,6,7,8,9]
b=prabhat.choice(a)
print(b)
if b>1:
    if b%2==0:
        print('not prime')
    else:
        print('prime')
else:
    print('prime')
