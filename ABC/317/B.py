N=int(input())
A=list(map(int,input().split()))
A.sort()
first=A.pop(0)
for v in A:
    first+=1
    if v!=first:
        print(first)
        exit()
print(first-1)
