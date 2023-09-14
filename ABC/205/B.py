import math
N=int(input())
A=list(map(int,input().split()))
if math.factorial(N)==math.prod(A):
    print('Yes')
else:
    print('No')
