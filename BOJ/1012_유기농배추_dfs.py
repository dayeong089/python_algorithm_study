import sys
r = sys.stdin.readline
sys.setrecursionlimit(10**9)

t = int(r())
result = []

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y, n, m):
    graph[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m:
            if graph[nx][ny] == 1:
                dfs(nx, ny, n, m)

for _ in range(t):
    m, n, k = map(int, r().split(" "))
    graph = []
    for _ in range(n):
        lst = [0]*m
        graph.append(lst)

    for _ in range(k):
        x, y = map(int, r().split(" "))
        graph[y][x] = 1

    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                dfs(i, j, n, m)
                cnt += 1
    result.append(cnt)

for i in result:
    print(i)
