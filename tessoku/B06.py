N=int(input())
A=list(map(int,input().split()))
win=[None]*(N+1)
lose=[None]*(N+1)
win[0]=0
lose[0]=0
for i in range(N):
	if A[i]==1:
		win[i+1]=win[i]+1
		lose[i+1]=lose[i]+0
	if A[i]==0:
		win[i+1]=win[i]+0
		lose[i+1]=lose[i]+1
Q=int(input())
for i in range(Q):
	a,b=map(int,input().split())
	x=win[b]-win[a-1]
	y=lose[b]-lose[a-1]
	if x>y:
		print('win')
	elif x<y:
		print('lose')
	else:
		print('draw')
