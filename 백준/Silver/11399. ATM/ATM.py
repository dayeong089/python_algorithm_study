import sys
r = sys.stdin.readline

n = int(r())
lst = list(map(int, r().split(" ")))
lst.sort()

ans = sum(lst) * len(lst)
for i in range(len(lst)-1, 0, -1):
    ans -= lst[i] * i
print(ans)