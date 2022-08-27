# 크루스칼 알고리즘 이용

import sys
r = sys.stdin.readline

def find_parent(parent, x):
    if parent[x]!=x:
        parent[x]=find_parent(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    x = find_parent(parent, x)
    y = find_parent(parent, y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

n, m = map(int, r().split(" "))
parent = [i for i in range(n+1)]
edges = []
total = 0
last = 0

for _ in range(m):
    a, b, cost = map(int, r().split(" "))
    edges.append((cost, a, b))

edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union(parent, a, b)
        total += cost
        last = cost

total -= last
print(total)
