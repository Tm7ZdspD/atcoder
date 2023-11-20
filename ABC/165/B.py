X=int(input())
p=100
y=0
while True:
	if p>=X:
		print(y)
		exit()
	y+=1
	p=p+p//100
