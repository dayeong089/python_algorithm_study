import sys
from collections import deque
r = sys.stdin.readline

n, m = map(int, r().split(" "))
graph = [list(map(int, r().rstrip())) for _ in range(n)]
visited = [[[0]*2 for _ in range(m)] for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

q = deque()
q.append((0,0,0))
visited[0][0][0] = 1

while q:
    x, y, b = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m:
            if graph[nx][ny] == 0 and visited[nx][ny][b] == 0:
                visited[nx][ny][b] = visited[x][y][b]+1
                q.append((nx,ny,b))
            elif graph[nx][ny] == 1 and b == 0:
                visited[nx][ny][1] = visited[x][y][0]+1
                q.append((nx,ny,1))

r1 = visited[n-1][m-1][0]
r2 = visited[n-1][m-1][1]

if r1 == 0 and r2 == 0: print("-1")
elif r1 == 0: print(r2)
elif r2 == 0: print(r1)
else: print(min(r1, r2))
