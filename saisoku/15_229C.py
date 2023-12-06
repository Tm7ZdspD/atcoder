N,W=map(int,input().split())
S=[]
for i in range(N):
	A,B=map(int,input().split())
	S.append([A,B])
S.sort(reverse=True)
ans=0
for i in range(N):
	a=S[i][0]
	b=S[i][1]
	if b<=W:
		ans+=a*b
		W-=b
	else:
		ans+=a*W
		break
print(ans)
