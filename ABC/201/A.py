A1,A2,A3=map(int, input().split())
A=[]
A.append(A1)
A.append(A2)
A.append(A3)
A.sort()
if A[2]-A[1]==A[1]-A[0]:
    print('Yes')
else:
    print('No')
