H,W,N=map(int,input().split())
A=[None]*N
B=[None]*N
C=[None]*N
D=[None]*N
for i in range(N):
	A[i],B[i],C[i],D[i]=map(int,input().split())
S=[[0]*(W+2) for _ in range(H+2)]
for i in range(N):
	S[A[i]][B[i]]+=1
	S[C[i]+1][D[i]+1]+=1
	S[A[i]][D[i]+1]-=1
	S[C[i]+1][B[i]]-=1
Z=[[0]*(W+2) for _ in range(H+2)]
for i in range(1,H+1):
	for j in range(1,W+1):
		Z[i][j]=Z[i][j-1]+S[i][j]
for j in range(1,W+1):
	for i in range(1,H+1):
		Z[i][j]=Z[i][j]+Z[i-1][j]
for i in range(1,H+1):
	for j in range(1,W+1):
		if j>=2:
			print(" ",end="")
		print(Z[i][j],end="")
	print("")
