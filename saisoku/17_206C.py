N=int(input())
A=list(map(int,input().split()))
from collections import defaultdict
cnt=defaultdict(int)
ans=N*(N-1)//2
for i in range(N):
	cnt[A[i]]+=1
for i in cnt.values():
	ans-=i*(i-1)//2
print(ans)
