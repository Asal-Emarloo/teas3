a=int(input("Enter number:"))
for i in range(a):
  if i%2==0:
    print("*",end=" ")
    
  elif i%2==1:
    print("#",end=" ")