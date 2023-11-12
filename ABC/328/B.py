N=int(input())
D=list(map(int,input().split()))
D.insert(0,None)
ans=0
for i in range(1,N+1):
	for j in range(1,D[i]+1):
		tmp=str(i)+str(j)
		tmp0=tmp[0]
		# print(tmp)
		flag=True
		for l in list(tmp):
			if int(tmp0)!=int(l):
				flag=False
		if flag:
			ans+=1
print(ans)
