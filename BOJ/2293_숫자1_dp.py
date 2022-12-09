import sys
r = sys.stdin.readline

n, k = map(int, r().split(" "))
coin_lst = [int(r()) for _ in range(n)]

dp = [0]*(k+1)
dp[0] = 1 #동전 1개만 쓰는 경우(처음으로 새로운 동전 종류 쓰는 경우)

#동전 종류 늘려가면서 경우 추가
#1원 동전만 쓰는 경우 + 1,2원 동전 쓰는 경우 
for i in coin_lst:
    for j in range(len(dp)):
        if j>=i:
            dp[j] += dp[j-i]

print(dp[k])
