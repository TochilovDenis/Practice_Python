x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if abs(x1 - x2) == abs(y1 - y2):
    print('YES')
else:
    print('NO')

# или без abs()

dx = x1 - x2
dy = y1 - y2
if (dx - dy == 0) or (dx + dy == 0):
    print("YES")
else:
    print("NO")