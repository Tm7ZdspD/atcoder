# N=int(input())
# ans=0
# for i in range(1,N+1):
#     if (i%3==0 and i%5==0) or i%3==0 or i%5==0:
#         continue
#     else:
#         ans+=i

# print(ans)

n=int(input())
ans=0
for i in range(1,n+1):
    if i%5!=0 and i%3!=0:
        ans+=i
print(ans)