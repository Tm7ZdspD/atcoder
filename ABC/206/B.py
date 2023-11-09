N=int(input())
ans=0
cnt=0
while True:
	ans+=1
	cnt+=ans
	if cnt>=N:
		print(ans)
		exit()
