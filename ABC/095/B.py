N,X=map(int,input().split())
m=[]
cnt=0
for _ in range(N):
    m.append(int(input()))
for v in m:
    X-=v
    cnt+=1
min_v=min(m)
print(cnt+X//min_v)
