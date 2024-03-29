import sys
r = sys.stdin.readline

n = int(r())
dp = [[0]*10 for _ in range(n+1)]
for i in range(1, 10):
    dp[1][i] = 1

for i in range(1, n):
    for j in range(10):
        if j==0:
            dp[i+1][1] += (dp[i][0]%1000000000)
        elif j==9:
            dp[i+1][8] += (dp[i][9]%1000000000)
        else:
            dp[i+1][j+1] += (dp[i][j]%1000000000)
            dp[i+1][j-1] += (dp[i][j]%1000000000)

print(sum(dp[n])%1000000000)
