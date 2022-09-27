import sys
r = sys.stdin.readline

n = int(r())
lst = [[0, 0, 0] for _ in range(n)]

for i in range(n):
    x, y, z = map(int, r().split(" "))

    if i==0:
        lst[i][0] = x
        lst[i][1] = y
        lst[i][2] = z
    else:
        lst[i][0] = x + min(lst[i-1][1], lst[i-1][2])
        lst[i][1] = y + min(lst[i-1][0], lst[i-1][2])
        lst[i][2] = z + min(lst[i-1][0], lst[i-1][1])

print(min(lst[n-1][0], lst[n-1][1], lst[n-1][2]))
