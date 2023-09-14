N=int(input())
a=list(map(int,input().split()))
a.sort(reverse=True)
Alice=0
Bob=0
flg=True
for p in a:
    if flg:
        Alice+=p
        flg=False
    else:
        Bob+=p
        flg=True
print(Alice-Bob)

