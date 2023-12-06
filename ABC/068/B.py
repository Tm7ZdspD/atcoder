N=int(input())
if N==1:
	print(1)
	exit()
ans=-1
max_cnt=0
for i in range(1,N+1):
	v=i
	cnt=0
	while v%2==0:
		cnt+=1
		v//=2
	if max_cnt<cnt:
		max_cnt=cnt
		ans=i	
print(ans)
