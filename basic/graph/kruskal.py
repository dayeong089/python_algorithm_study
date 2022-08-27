# 크루스칼 알고리즘

import sys
r = sys.stdin.readline

def find_parent(parent, x):
    if parent[x]!=x:
        parent[x]=find_parent(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    x = find_parent(parent, x)
    y = find_parent(parent, y)
    if x>y:
        parent[x]=y
    else:
        parent[y]=x

v, e = map(int, r().split(" "))
parent = [i for i in range(v+1)]
cost = 0
edges = []

for _ in range(e):
    a, b, c = map(int, r().split(" "))
    edges.append((c, a, b))

edges.sort()

for edge in edges:
    c, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union(parent, a, b)
        cost += c

print(cost)
