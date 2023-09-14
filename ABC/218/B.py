P=list(map(int,input().split()))
chars='abcdefghijklmnopqrstuvwxyz'
ans=''
for i in P:
    ans+=chars[i-1]
print(ans)
