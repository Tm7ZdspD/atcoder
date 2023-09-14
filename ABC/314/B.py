N=int(input())
d={}
min_size=100
for i in range(1,N+1):
    c=int(input())
    d[i]=list(map(int,input().split()))
X=int(input())
for i in range(1,N+1):
    if X not in d[i]:
        d.pop(i)
    else:
        if min_size>len(d[i]):
            min_size=len(d[i])
ans=[]
for i in d:
    if len(d[i])==min_size:
        ans.append(i)
print(len(ans))
print(*ans)
