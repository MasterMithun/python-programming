j=input().split()
j=list(map(int,j))
if(j[0]%2==0):
  k=j[0]+1
  while(k<j[1]):
    if(j[1]%2==0):
      if(j[1]==k+1):
        print(k,end='')
      else:
        print(k,end=' ')
    else:
      if(j[1]==k+2):
        print(k,end='')
      else:
        print(k,end=' ')
    k=k+2
elif(j[0]%2!=0):
  k=j[0]+2
  while(k<j[1]):
    if(j[1]%2==0):
      if(j[1]==k+1):
        print(k,end='')
      else:
          print(k,end=' ')
    else:
      if(j[1]==k+2):
        print(k,end='')
      else:
        print(k,end=' ')
    k=k+2
