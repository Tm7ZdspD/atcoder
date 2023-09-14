H, A = map(int, input().split())
if H % A ==0:
    print(H // A)
else:
    print(H // A + 1)

# count = 0

# while True:
#     count += 1
#     H = H - A

#     if H <= 0:
#         print(count)
#         exit()
