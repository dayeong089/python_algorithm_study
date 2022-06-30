''''
그래프 정보를 입력받고, dfs & bfs 탐색 결과를 출력하는 문제
''''
import sys
from collections import deque
r = sys.stdin.readline

n, m, v = map(int, r().split(" "))
graph = [[] for _ in range(n+1)]

for i in range(m):
    x, y = map(int, r().split(" "))
    graph[x].append(y)
    graph[y].append(x)

for g in graph:
    g.sort()

visited = [False]*(n+1)
visited2 = [False]*(n+1)

def dfs(graph, start, visited):
    print(start, end=' ')
    visited[start] = True
    for i in range(len(graph[start])):
        now = graph[start][i]
        if visited[now] == False:
            dfs(graph, now, visited)

def bfs(graph, visited):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        start = queue.popleft()
        print(start, end=' ')
        for i in range(len(graph[start])):
            now = graph[start][i]
            if visited[now] == False:
                queue.append(now)
                visited[now] = True

dfs(graph, v, visited)
print()
bfs(graph, visited2)
print()
