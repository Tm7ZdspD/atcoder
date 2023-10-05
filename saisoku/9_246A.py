x=[None]*3
y=[None]*3
for i in range(3):
	x[i],y[i]=map(int,input().split())
if x[0]==x[1]:
	print(x[2], end=" ")
else:
	if x[1]==x[2]:
		print(x[0], end=" ")
	else:
		print(x[1], end=" ")
if y[0]==y[1]:
	print(y[2])
else:
	if y[1]==y[2]:
		print(y[0])
	else:
		print(y[1])
