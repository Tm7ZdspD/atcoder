D=int(input())
N=int(input())
S=[0]*(D+2)
S[0]=0
for i in range(N):
	L,R=map(int,input().split())
	S[L]+=1
	S[R+1]-=1
SS=[None]*(D+1)
SS[0]=0
for i in range(1,D+1):
	SS[i]=SS[i-1]+S[i]
for i in range(1,D+1):
	print(SS[i])
