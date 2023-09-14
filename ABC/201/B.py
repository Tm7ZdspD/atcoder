N=int(input())
ST={}
for _ in range(N):
    S,T=map(str,input().split())
    ST[S]=int(T)
sort_ST=sorted(ST.items(),key=lambda x:x[1],reverse=True)
print(sort_ST[1][0])
