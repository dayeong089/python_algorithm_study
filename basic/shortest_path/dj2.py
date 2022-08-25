# 다익스트라 알고리즘(2)
# 우선순위 큐 - heapq를 사용 > 더 효율적
# 시간 복잡도 > O(ElogV) (V=노드의 개수, E=간선의 개수)

import sys
import heapq
r = sys.stdin.readline
INF = int(1e9)

n, m = map(int, r().split(" "))
start = int(r())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1) 
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, r().split(" "))
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            if distance[i[0]] > dist + i[1]:
                distance[i[0]] = dist + i[1]
                heapq.heappush(q, (dist+i[1], i[0]))

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("infinity")
    else:
        print(distance[i])
