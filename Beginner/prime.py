n=int(input("enter the value"))
a=0
for i in range (1,n):
  if(n%i==0):
    a=a+1  
    if(a==2):
      print("not a prime nnumber")
    else:
      print("it is prime number")
