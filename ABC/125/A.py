A,B,T=map(int,input().split())
C=1
ans=0
d=A
while T+0.5>d:
	ans+=B
	C+=1
	d=A*C
print(ans)
