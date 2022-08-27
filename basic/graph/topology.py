# 위상 정렬 코드

import sys
from collections import deque
r = sys.stdin.readline

v, e = map(int, r().split(" "))
graph = [[] for _ in range(v+1)]
indegree = [0] * (v+1)

for _ in range(e):
    a, b = map(int, r().split(" "))
    graph[a].append(b)
    indegree[b] += 1

def topology():
    result = []
    q = deque()
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    
    print(result)

topology()
