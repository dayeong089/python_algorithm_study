import sys
r = sys.stdin.readline
sys.setrecursionlimit(10**9)

N, M, R = map(int, r().split(" "))
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
cnt = 1

for _ in range(M):
    u, v = map(int, r().split(" "))
    graph[u].append(v)
    graph[v].append(u)

for i in graph:
    i.sort()

def dfs(start):
    global cnt
    visited[start] = cnt
    for i in graph[start]:
        if visited[i] == 0:
            cnt += 1
            dfs(i)

dfs(R)

for i in range(1, len(visited)):
    print(visited[i])
