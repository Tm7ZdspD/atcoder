A,B,K=map(int,input().split())
ans=[]
for i in range(K):
    if A+i<=B:
        ans.append(A+i)
for i in range(K,0,-1):
    if B-i+1 not in ans and B-i+1>=A:
        ans.append(B-i+1)

for j in ans:
    print(j)