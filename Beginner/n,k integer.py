end=int(raw_input())
value=int(raw_input())
z=[]
sum=0
for i in range(0,end):
	k=int(raw_input())
	z.append(k)
for j in range(0,value):
	sum+=z[j]
print(sum)
