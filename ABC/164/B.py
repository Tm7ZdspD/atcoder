A,B,C,D=map(int,input().split())
a_attack_flag=True

while True:
    if a_attack_flag:
        C-=B
        if C<=0:
            print('Yes')
            exit()
        a_attack_flag=False
    else:
        A-=D
        if A<=0:
            print('No')
            exit()
        a_attack_flag=True