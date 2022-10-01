import sys
r = sys.stdin.readline

n = int(r())
lst = list(map(int, r().split(" ")))
cnt = [1]*n

for i in range(1, n):
    x = []
    for j in range(0, i):
        if lst[j] < lst[i]:
            x.append(cnt[j])
    if len(x)!=0:
        cnt[i] = max(x)+1

print(max(cnt))
