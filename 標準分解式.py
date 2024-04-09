import random
num=random.randint(0,99)
ori=num
i=2
print(num,end="=")

while (i<=num):
    if num%i==0:
        if num==i:
            print(i)
            break
        else:
            num=num/i
            print(i,end="x")
    else:
        i=i+1
    
    
