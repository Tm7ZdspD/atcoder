A,B=map(int,input().split())
import math
for i in range(1,1501):
	a=math.floor(i*0.08)
	b=math.floor(i*0.10)
	if a==A and b==B:
		print(i)
		exit()
print(-1)
