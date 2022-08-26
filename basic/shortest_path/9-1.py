# 다익스트라 알고리즘을 활용

import sys
import heapq
r = sys.stdin.readline
INF = int(1e9)

n, m = map(int, r().split(" "))
graph = [[] for _ in range(n+1)]
distance = [INF]*(n+1)

for i in range(m):
    a, b = map(int, r().split(" "))
    graph[a].append((b, 1))
    graph[b].append((a, 1))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

x, k = map(int, r().split(" "))

dijkstra(1)
result1 = distance[k]

distance = [INF]*(n+1)
dijkstra(k)
result2 = distance[x]

result = result1+result2
if result>=INF:
    print("-1")
else:
    print(result)
