N=int(input())
S=input()
chars='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ans=''
for v in S:
    i=chars.find(v)
    new_i=i+N
    if new_i>=26:
        new_i=new_i-26
    ans+=chars[new_i]
print(ans)
