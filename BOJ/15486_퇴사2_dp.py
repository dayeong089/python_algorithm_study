import sys
r = sys.stdin.readline

n = int(r())
t = []
p = []
dp = [0]*(n+1)

for _ in range(n):
    x, y = map(int, r().split(" "))
    t.append(x)
    p.append(y)

k = 0
for i in range(n):
    k = max(k, dp[i])
    if i+t[i] <= n:
        dp[i+t[i]] = max(dp[i+t[i]], k+p[i])

print(max(dp))
