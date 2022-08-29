# 위상 정렬 알고리즘 이용

import sys
from collections import deque
r = sys.stdin.readline

n = int(r())
graph = [[] for _ in range(n+1)]
time = [0]*(n+1)
result = [0]*(n+1)
indegree = [0]*(n+1)

for i in range(1, n+1):
    lst = list(map(int, r().split(" ")))
    time[i] = lst[0]
    result[i] = lst[0]
    for j in range(1, len(lst)-1):
        graph[lst[j]].append(i)
    indegree[i] = len(lst)-2

def topology():
    q = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for i in graph[now]:
            indegree[i] -= 1
            result[i] = max(result[i], result[now]+time[i])
            if indegree[i]==0:
                q.append(i)

topology()

for i in range(1, n+1):
    print(result[i])
