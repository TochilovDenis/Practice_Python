x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

dxy1 = x1 + y1
dxy2 = x2 + y2

if dxy1 % 2 == 0 and dxy2 % 2 != 0 and (y2 == 5 or y2 == 4):
    print("NO")
elif (dxy1 + dxy2) % 2 != 0:
    print("YES")
else:
    print("NO")

# или с abs()

dx = abs(x1 - x2)
dy = abs(y1 - y2)

if dx == 1 and dy == 2 or dx == 2 and dy == 1:
    print('YES')
else:
    print('NO')