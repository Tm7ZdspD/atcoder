N,A,B=map(int,input().split())
ans=0
for i in range(1,N+1):
	x=[int(a) for a in str(i)]
	sum_x=sum(x)	
	if A<=sum_x and sum_x<=B:
		ans+=i
print(ans)
