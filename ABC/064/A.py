r,g,b = map(str, input().split())
num = int(r+g+b)

print("YES" if num%4==0 else "NO")