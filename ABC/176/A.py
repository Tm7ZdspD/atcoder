# N,X,T = map(int, input().split())

# count = 0
# flag = True

# while flag:
#     count += 1
#     N = N - X

#     if N <= 0:
#         flag = False

# print(count*T)

n,x,t=map(int,input().split())
if n%x==0:
    print(t*n//x)
else:
    print(t*(n//x+1))