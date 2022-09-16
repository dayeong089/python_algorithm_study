import sys
from collections import deque
r = sys.stdin.readline

N, M, R = map(int, r().split(" "))
graph = [[] for _ in range(N+1)]
visited = [0]*(N+1)
cnt = 1

for _ in range(M):
    u, v = map(int, r().split(" "))
    graph[u].append(v)
    graph[v].append(u)

for i in graph:
    i.sort()

def bfs(start):
    global cnt
    q = deque()
    q.append(start)
    visited[start] = cnt

    while q:
        x = q.popleft()
        
        for i in graph[x]:
            if visited[i] == 0:
                cnt += 1
                visited[i] = cnt
                q.append(i)

bfs(R)

for i in range(1, len(visited)):
    print(visited[i])
