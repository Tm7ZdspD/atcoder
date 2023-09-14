N = int(input())
A = list(map(int, input().split()))
B = []
for i in range(N):
    tmp = 0
    for j in range(7):
        tmp += A[i*7+j]
    B.append(tmp)

print(*B)