N,X,T=map(int,input().split())
ans=T
cnt=X
while True:
	if cnt>=N:
		print(ans)
		exit()
	ans+=T
	cnt+=X
