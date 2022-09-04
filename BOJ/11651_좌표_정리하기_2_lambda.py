# sort, lambda

import sys
r = sys.stdin.readline

lst = []
n = int(r())
for _ in range(n):
    x, y = map(int, r().split(" "))
    lst.append((x, y))

lst.sort(key=lambda x:(x[1], x[0]))

for i in lst:
    print(i[0], i[1])
