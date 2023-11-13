N=int(input())
A=list(map(int,input().split()))
X=int(input())
sum_A=sum(A)
cnt=X//sum_A
ans=cnt*N
sum_B=cnt*sum_A
for v in A:
	ans+=1
	sum_B+=v
	if X<sum_B:
		print(ans)
		exit()
