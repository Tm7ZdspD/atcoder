A,B=map(int,input().split())
ans=0
for i in range(A,B+1):
	a1=str(i)[0]	
	a2=str(i)[1]	
	a4=str(i)[3]	
	a5=str(i)[4]	
	if a1==a5 and a2==a4:
		ans+=1
print(ans)
