S=input()
if S[0]=='A':
    string1=S[2:-1]
    if string1.count('C')==1:
        string2=S.replace(S[0],'')
        string2=string2.replace('C','')
        if string2.islower():
            print('AC')
            exit()
print('WA')

