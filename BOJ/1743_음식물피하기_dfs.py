import sys
r = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m, k = map(int, r().split(" "))
graph = [[0]*m for _ in range(n)]
lst = []
value = 0

for _ in range(k):
    a, b = map(int, r().split(" "))
    graph[a-1][b-1] = 1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y):
    global value
    value += 1
    graph[x][y] += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m:
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y]+1
                dfs(nx, ny)

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            value = 0
            dfs(i, j)
            lst.append(value)

print(max(lst))
