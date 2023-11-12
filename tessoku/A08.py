H,W=map(int,input().split())
X=[None]*H
Z=[[0]*(W+1) for _ in range(H+1)]
for i in range(H):
	X[i]=list(map(int,input().split()))
for i in range(1,H+1):
	for j in range(1,W+1):
		Z[i][j]=Z[i][j-1]+X[i-1][j-1]
for j in range(1,W+1):
	for i in range(1,H+1):
		Z[i][j]=Z[i][j]+Z[i-1][j]
Q=int(input())
A=[None]*Q
B=[None]*Q
C=[None]*Q
D=[None]*Q
for i in range(Q):
	A[i],B[i],C[i],D[i]=list(map(int,input().split()))
for i in range(Q):
	print(Z[C[i]][D[i]]+Z[A[i]-1][B[i]-1]-Z[A[i]-1][D[i]]-Z[C[i]][B[i]-1])
