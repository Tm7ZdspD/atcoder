r,g,b=map(str,input().split())
S=int(r+g+b)
if S%4==0:
	print('YES')
else:
	print('NO')
