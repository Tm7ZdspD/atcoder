N=int(input())
P=list(map(int,input().split()))
if len(P)==1:
    print(0)
    exit()
p1=P[0]
p_ex=[]
for i in range(1,N):
    p_ex.append(P[i])
max_p_ex=max(p_ex)
if p1>max_p_ex:
    print(0)
else:
    print(max_p_ex-p1+1)
