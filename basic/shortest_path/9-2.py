# 다익스트라 알고리즘 활용

import sys
import heapq
r = sys.stdin.readline
INF = int(1e9)

n, m, start = map(int, r().split(" "))
graph = [[] for _ in range(n+1)]
distance = [INF]*(n+1)

for _ in range(m):
    a, b, c = map(int, r().split(" "))
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = dist+i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)
cnt = 0
total = []
for i in range(1, n+1):
    if distance[i]!=INF:
        cnt+=1
        total.append(distance[i])
print(cnt-1, max(total))
