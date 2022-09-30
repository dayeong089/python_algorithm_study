import sys
from collections import deque
r = sys.stdin.readline

m, n = map(int, r().split(" "))
graph = []
for _ in range(n):
    lst = list(map(int, r().split(" ")))
    graph.append(lst)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs():
    q = deque()
    for i in onelst:
        q.append((i[0], i[1], 0))
    while q:
        x, y, cnt = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and graph[nx][ny]==0:
                q.append((nx, ny, cnt+1))
                graph[nx][ny]=cnt+1
            
check = True
onelst = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            check = False
        elif graph[i][j] == 1:
            onelst.append((i, j))

if check == True:
    print("0")
else:
    bfs()
    check2 = True
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                check2 = False
                break
    if check2 == False:
        print("-1")
    else:
        print(max([max(row) for row in graph]))
