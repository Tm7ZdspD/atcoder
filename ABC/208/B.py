P=int(input())
import math
ans=0
for i in range(10,0,-1):
	c=math.factorial(i)
	if P>=c:
		num=P//c	
		P-=num*c
		ans+=num
print(ans)
