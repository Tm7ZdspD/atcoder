N=input()
strLen=len(N)
strLen-=1
ans=0
for v in N:
	tmp=int(v)*(2**strLen)
	ans+=tmp
	strLen-=1
print(ans)
