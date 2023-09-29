N=int(input())
A=list(map(int,input().split()))
ans=0
for v in A:
	if v>=10:
		ans+=v-10
print(ans)
