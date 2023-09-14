a,b=map(int, input().split())
A=''
B=''
for v in range(b):
    A+=str(a)
for v in range(a):
    B+=str(b)
if A<B:
    print(A)
else:
    print(B)
