N=int(input())
X=[None]*N
Y=[None]*N
for i in range(N):
	X[i],Y[i]=map(int,input().split())
S=[[0]*1501 for _ in range(1501)]
for i in range(N):
	S[X[i]][Y[i]]+=1
Z=[[0]*1501 for _ in range(1501)]
for i in range(1,1501):
	for j in range(1,1501):
		Z[i][j]=Z[i][j-1]+S[i][j]	
for j in range(1,1501):
	for i in range(1,1501):
		Z[i][j]=Z[i-1][j]+Z[i][j]
Q=int(input())
a=[None]*Q
b=[None]*Q
c=[None]*Q
d=[None]*Q
for i in range(Q):
	a[i],b[i],c[i],d[i]=map(int,input().split())
for i in range(Q):
	print(Z[c[i]][d[i]]+Z[a[i]-1][b[i]-1]-Z[c[i]][b[i]-1]-Z[a[i]-1][d[i]])
