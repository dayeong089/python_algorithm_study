# find 연산을 이용한 사이클 판별

import sys
r = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
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

for _ in range(e):
    a, b = map(int, r().split(" "))
    if find_parent(parent, a) == find_parent(parent, b):
        print("cycle")
        break
    else:
        union(parent, a, b)
