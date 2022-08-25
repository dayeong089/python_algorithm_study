# 플로이드 워셜 알고리즘

import sys
r = sys.stdin.readline
INF = int(1e9)

n = int(r())
m = int(r())
graph = [[INF]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        if i==j:
            graph[i][j] = 0

for i in range(m):
    a, b, c = map(int, r().split(" "))
    graph[a][b] = c

for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            graph[j][k] = min(graph[j][k], graph[j][i]+graph[i][k])

for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == INF:
            print("infinity", end=" ")
        else:
            print(graph[i][j], end=" ")
    print()
