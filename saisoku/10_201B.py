N=int(input())
d={}
for _ in range(N):
	S,T=map(str,input().split())
	d[S]=int(T)
d=sorted(d.items(), key=lambda t: t[1], reverse=True)
print(d[1][0])
