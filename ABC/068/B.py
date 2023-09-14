N=int(input())
if N==1:
	print(1)
	exit()
ans=0
div_cnt=0
for i in reversed(range(1,N+1)):
	tmp=i
	cnt=0
	while True:
		if tmp%2==0:
			cnt+=1
			tmp//=2
		else:
			break
	if cnt>div_cnt:
		div_cnt=cnt
		ans=i
print(ans)
