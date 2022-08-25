# 다익스트라 알고리즘(1)
# 시간 복잡도 > O(V^2) (V=노드의 개수)
# 전체 노드의 개수가 5000개 이하라면 사용 가능

import sys
r = sys.stdin.readline
INF = int(1e9)

n, m = map(int, r().split(" "))
start = int(r())
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
distance = [INF]*(n+1)

for i in range(m):
    a, b, c = map(int, r().split(" "))
    graph[a].append((b, c))

def get_smallest_node():
    min_dis = INF
    idx = 0
    for i in range(1, n+1):
        if not visited[i]:
            if distance[i] < min_dis:
                min_dis = distance[i]
                idx = i
    return idx

def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for i in graph[start]:
        distance[i[0]] = i[1]
    for i in range(n-1):
        now = get_smallest_node()
        visited[now] = True
        for j in graph[now]:
            distance[j[0]] = min(distance[j[0]], distance[now]+j[1])

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])
