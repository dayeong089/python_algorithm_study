import sys
r = sys.stdin.readline

n, m = map(int, r().split(" "))
graph = [list(r().rstrip()) for _ in range(m)]

white_value = 0
black_value = 0
value = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y, team):
    global value
    value += 1
    graph[x][y] = value

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<m and 0<=ny<n:
            if graph[nx][ny] == team:
                dfs(nx, ny, team)

for i in range(m):
    for j in range(n):
        if graph[i][j] == 'W':
            value = 0
            dfs(i, j, 'W')
            white_value += (value*value)
        elif graph[i][j] == 'B':
            value = 0
            dfs(i, j, 'B')
            black_value += (value*value)

print(white_value, black_value)
