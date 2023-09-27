N=int(input())
ans=''
while True:
	if N<=0:
		ansLen=len(ans)
		if ansLen<=10:
			zeroCnt=10-ansLen
			ans='0'*zeroCnt+ans
		print(ans)
		exit()
	else:
		ans=str(N%2)+ans
		N//=2
