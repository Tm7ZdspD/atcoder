S = input()

if 'R' not in S:
    print(0)
else:
    if S[0] == 'R' and S[1] == 'R' and S[2] == 'R':
        print(3)
    elif S[0] == 'R' and S[1] == 'R':
        print(2)
    elif S[1] == 'R' and S[2] == 'R':
        print(2)
    else:
        print(1)
