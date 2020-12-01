x, y = map(int, input().split())

if x == y:
    print(x)
    exit(0)

ans = 0
a = list()
if y > x:
    xy = y % x
    
xy = x % y

for i in range(xy, 0, -1):
    if xy % i == 0:
        if y % i == 0:
            ans = i
            break

print(ans)
