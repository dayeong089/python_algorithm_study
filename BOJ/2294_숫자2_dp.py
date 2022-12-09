#첫 코드 - 시간 초과
import sys
r = sys.stdin.readline

n, k = map(int, r().split(" "))
coin_lst = [int(r()) for _ in range(n)]
dp = [[] for _ in range(k+1)]
dp[0].append(0)

for i in coin_lst:
    for j in range(len(dp)):
        if j>=i:
            if len(dp[j-i])!=0:
                min_value = min(dp[j-i])
                dp[j].append(min_value+1)

if len(dp[k]) == 0:
    print("-1")
else:
    print(min(dp[k]))
        
#수정한 코드
import sys
r = sys.stdin.readline

n, k = map(int, r().split(" "))
coin_lst = [int(r()) for _ in range(n)]
dp = [[10001] for _ in range(k+1)]
dp[0][0] = 0

for i in coin_lst:
    for j in range(len(dp)):
        if j>=i:
            dp[j][0] = min(dp[j][0], dp[j-i][0]+1)

if dp[k][0] == 10001:
    print("-1")
else:
    print(dp[k][0])
