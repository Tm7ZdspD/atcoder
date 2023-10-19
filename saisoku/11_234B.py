N=int(input())
ans=0
x=[None]*N
y=[None]*N
for i in range(N):
	x[i],y[i]=map(int,input().split())
import math
for i in range(N):
	for j in range(i+1,N):
		tmp=math.sqrt((x[j]-x[i])**2+(y[j]-y[i])**2)
		ans=max(tmp,ans)
print(ans)
