#1번 풀이 - 재귀함수 이용 > dist가 0인 경우를 생각해야함
import sys
r = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(r())
graph = [list(map(int, r().split(" "))) for _ in range(n)]
result = [[-1]*n for _ in range(n)]

def dp(x, y):
    if x == n-1 and y == n-1:
        result[x][y] = 1
        return result[x][y]

    dist = graph[x][y]
    nx = x+dist
    ny = y+dist
    if dist == 0:
        return 0
    a = 0
    b = 0

    if nx<n:
        if result[nx][y] != -1:
            a = result[nx][y]
        else:
            a = dp(nx, y)
    if ny<n:
        if result[x][ny] != -1:
            b = result[x][ny]
        else:
            b = dp(x, ny)

    result[x][y] = a+b
    return result[x][y]
print(dp(0,0))

#2번 풀이 - 반복문 이용
n = int(input())
a = list(list(map(int,input().split())) for _ in range(n))
dp = [[0]*n for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if i == n - 1 and j == n - 1:
            print(dp[i][j])
            break
        if i + a[i][j] < n:
            dp[i+a[i][j]][j] += dp[i][j]
        if j + a[i][j] < n:
            dp[i][j+a[i][j]] += dp[i][j]
