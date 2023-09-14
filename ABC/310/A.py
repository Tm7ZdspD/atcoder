N,P,Q=map(int,input().split())
D=list(map(int,input().split()))
min_D=min(D)
if P<=Q+min_D:
    print(P)
else:
    print(Q+min_D)
