import sys
from collections import deque
r = sys.stdin.readline

a = int(r())
result = []

for _ in range(a):
    n, m = map(int, r().split(" "))
    imp = list(map(int, r().split(" ")))
    lst = []
    for i in range(len(imp)):
        lst.append((imp[i], i))
    q = deque(lst)
    num = lst[m]
    cnt = 0

    while q:
        max_value = max(lst)
        x = q.popleft()
        if max_value[0] == x[0]:
            cnt += 1
            if x == num:
                result.append(cnt)
            lst.remove(max_value)
        else:
            q.append(x)

for i in result:
    print(i)
