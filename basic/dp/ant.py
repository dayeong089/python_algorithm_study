import sys
r = sys.stdin.readline

n = int(r())
lst = list(map(int, r().split(" ")))
cnt = [0]*101

cnt[1]= lst[0]
cnt[2] = max(lst[0], lst[1])

for i in range(3, n+1):
    cnt[i] = max(cnt[i-1], cnt[i-2]+lst[i-1])

print(cnt[n])
