import sys
r = sys.stdin.readline

n = int(r())
graph = []
for _ in range(n):
    lst = list(map(int, r().rstrip()))
    graph.append(lst)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
cnt = 0
num = 0
result = []

def dfs(x, y):
    global num
    num += 1 # 단지내 집 수 늘리기
    graph[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<n:
            if graph[nx][ny] == 1:
                dfs(nx, ny)

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            cnt += 1 # 단지 수 늘리기
            num = 0 # 단지 집 수 초기화
            dfs(i, j)
            result.append(num)

print(cnt)
result.sort()
for i in result:
    print(i)
