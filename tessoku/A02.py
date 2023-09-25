N,X=map(int,input().split())
A=list(map(int,input().split()))
for v in A:
	if v==X:
		print('Yes')	
		exit()
print('No')
