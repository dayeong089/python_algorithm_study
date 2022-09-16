import sys
from collections import deque
r = sys.stdin.readline

n = int(r())
m = int(r())
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
cnt = 0

for _ in range(m):
    x, y = map(int, r().split(" "))
    graph[x].append(y)
    graph[y].append(x)

def bfs(start):
    global cnt
    q = deque()
    q.append(start)
    visited[start] = True

    while q:
        now = q.popleft()
        for i in graph[now]:
            if visited[i] == False:
                visited[i] = True
                q.append(i) 
                cnt += 1

bfs(1)
print(cnt)
