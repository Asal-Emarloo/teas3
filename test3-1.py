import random
a=int(input("Enter a number:"))
b=[]
while len(b)<a:
    x=random.randint(0,10)
    if x not in b:
        b.append(x)
print(b)        

