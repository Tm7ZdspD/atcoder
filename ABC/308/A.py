S=list(map(int, input().split()))

tmpS=sorted(S)

if tmpS!=S:
    print("No")
    exit()

for i in S:
    if i<100 or 675<i or i%25!=0:
        print("No")
        exit()

print("Yes")