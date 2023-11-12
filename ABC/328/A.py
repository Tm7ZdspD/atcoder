N,X=map(int,input().split())
S=list(map(int,input().split()))
ans=0
for v in S:
	if v<=X:
		ans+=v
print(ans)
