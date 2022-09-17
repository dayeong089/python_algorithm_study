import sys
from collections import deque
r = sys.stdin.readline

n, m = map(int, r().split(" "))
graph = []
for _ in range(n):
    lst = list(map(int, r().rstrip()))
    graph.append(lst)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y, n, m):
    q = deque()
    q.append((x, y))

    while q:
        x1, y1 = q.popleft()
        for i in range(4):
            nx = x1 + dx[i]
            ny = y1 + dy[i]
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = graph[x1][y1]+1
                    q.append((nx, ny))
                
bfs(0, 0, n, m)
print(graph[n-1][m-1])
