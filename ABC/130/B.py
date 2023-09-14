N,X=map(int,input().split())
L=list(map(int,input().split()))
point=0
ans=0
for l in L:
	if point<=X:
		ans+=1
	point+=l
if point<=X:
	ans+=1
print(ans) 
