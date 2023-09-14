import math
P=int(input())
ans=0
for i in reversed(range(1,11)):
    coin=math.factorial(i)
    if P>=coin:
        num=P//coin
        P-=coin*num
        ans+=num

print(ans)