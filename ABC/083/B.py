N,A,B=map(int,input().split())

# ans=0
# for i in range(1,N+1):
#     tmp=list(map(int, str(i)))
#     tmp_sum=sum(tmp)
#     if A <= tmp_sum and tmp_sum <= B:
#         ans+=i

# print(ans)

def calc_sum_digits(n):
    sum_digit=0
    while n>0:
        sum_digit+=n%10
        n//=10
    return sum_digit

ans=0

for i in range(1,N+1):
    if A<=calc_sum_digits(i)<=B:
        ans+=i

print(ans)
