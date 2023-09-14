N,M=map(int,input().split())
eatedList=list(map(str, input().split()))
menuList=list(map(str, input().split()))
priceList=list(map(int, input().split()))
price=0

for i,x in enumerate(eatedList):
    flag=x in menuList
    if flag:
        priceIndex=menuList.index(x)
        price+=priceList[priceIndex+1]
    else:
        price+=priceList[0]

print(price)