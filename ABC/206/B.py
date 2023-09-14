N=int(input())
savings=0
for i in range(1,N+1):
    savings+=i
    if savings>=N:
        print(i)
        exit()