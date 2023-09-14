import math
N,D=map(int,input().split())
cnt=0
for i in range(N):
    X,Y=map(int,input().split())
    tmp=math.sqrt(X**2+Y**2)
    if tmp<=float(D):
        cnt+=1
print(cnt)
