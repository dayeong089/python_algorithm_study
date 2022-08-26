# 플로이드 워셜 알고리즘을 활용

import sys
r = sys.stdin.readline
INF = int(1e9)

n, m = map(int, r().split(" "))
graph = [[INF]*(n+1) for _ in range(n+1)]

for i in range(m):
    a, b = map(int, r().split(" "))
    graph[a][b]=1
    graph[b][a]=1

for i in range(1, n+1):
    for j in range(1, n+1):
        if i==j:
            graph[i][j]=0

for x in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][x]+graph[x][j])

x, k = map(int, r().split(" "))

distance = graph[1][k] + graph[k][x]
if distance >= INF:
    print("-1")
else:
    print(distance)
