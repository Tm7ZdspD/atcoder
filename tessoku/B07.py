T=int(input())
N=int(input())
L=[None]*N
R=[None]*N
for i in range(N):
	L[i],R[i]=map(int,input().split())
S=[0]*(T+1)
for i in range(N):
	S[L[i]]+=1
	S[R[i]]-=1
ans=[0]*(T+1)
ans[0]=S[0]
for i in range(1,T+1):
	ans[i]=ans[i-1]+S[i]
for i in range(T):
	print(ans[i])
