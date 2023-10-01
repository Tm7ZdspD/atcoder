P=list(map(int,input().split()))
chars=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',]
ans=''
for v in P:
	i=int(v)-1
	ans+=chars[i]
print(ans)
