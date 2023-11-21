A,B,K=map(int,input().split())
ans=[]
for i in range(K):
	if A+i<=B:
		ans.append(A+i)
for i in range(K):
	v=B-i
	if v not in ans and A<=v:
		ans.append(v)
ans.sort()
for v in ans:
	print(v)
