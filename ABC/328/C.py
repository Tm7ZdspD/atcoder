N,Q=map(int,input().split())
S=input()
for i in range(Q):
	l,r=map(int,input().split())
	tmp_str=S[l-1:r]
	ans=0
	for j in range(len(tmp_str)):
		if j+1<len(tmp_str):
			if tmp_str[j]==tmp_str[j+1]:
				ans+=1
	print(ans)
