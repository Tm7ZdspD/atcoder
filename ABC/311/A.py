N=int(input())
S=input()
cnt=0
flg_A=False
flg_B=False
flg_C=False
for v in S:
    if v=='A':
        flg_A=True
    if v=='B':
        flg_B=True
    if v=='C':
        flg_C=True
    cnt+=1
    if flg_A and flg_B and flg_C:
        print(cnt)
        exit()




