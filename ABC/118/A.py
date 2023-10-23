A,B=map(int,input().split())
for i in range(1,B+1):
	if B%i==0 and i==A:
		print(A+B)
		exit()
print(B-A)
