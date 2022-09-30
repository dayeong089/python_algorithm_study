import sys
from collections import deque
r = sys.stdin.readline

m, n, h = map(int, r().split(" "))
graph = [[list(map(int, r().split(" "))) for _ in range(n)] for _ in range(h)]

dx = [0, 0, 0, 0, 1, -1]
dy = [0, 0, 1, -1, 0, 0]
dz = [1, -1, 0, 0, 0, 0]

q = deque()
zero = []
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                q.append((i, j, k, 0))
            elif graph[i][j][k] == 0:
                zero.append(1)

if len(zero)==0:
    print("0")
    sys.exit(0)

while q:
    x, y, z, cnt = q.popleft()
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]
        if 0<=nx<h and 0<=ny<n and 0<=nz<m and graph[nx][ny][nz]==0:
            graph[nx][ny][nz]=cnt+1
            q.append((nx,ny,nz,cnt+1))

for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 0:
                print("-1")
                sys.exit(0)

max_lst = []
for x in graph:
    for y in x:
        max_lst.append(max(y))
print(max(max_lst))
