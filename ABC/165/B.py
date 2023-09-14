import math

X=int(input())
price=100
year=0

while price<X:
    year+=1
    # 下記コメントアウトのコードでは、値が"974755271730884810"の時にエラーになる
    # https://qiita.com/takepan/items/b570bca083b7aed31fbe
    # price=int(price*1.01)
    # price=math.floor(price*1.01)
    price=price+price//100

print(year)