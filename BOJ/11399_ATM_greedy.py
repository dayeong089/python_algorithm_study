# code1
import sys
r = sys.stdin.readline

n = int(r())
lst = list(map(int, r().split(" ")))
lst.sort()

x = 0
for i in range(len(lst)):
    now = 0
    for j in range(i+1):
        now += lst[j]
    x += now
print(x)

# code2 - 시간 단축
import sys
r = sys.stdin.readline

n = int(r())
lst = list(map(int, r().split(" ")))
lst.sort()

ans = sum(lst) * len(lst)
for i in range(len(lst)-1, 0, -1):
    ans -= lst[i] * i
print(ans)
