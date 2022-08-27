# 서로소 집합 알고리즘 이용

import sys
r = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
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

for _ in range(m):
    oper, a, b = map(int, r().split(" "))
    if oper==0:
        union(parent, a, b)
    elif oper==1:
        if find_parent(parent, a) == find_parent(parent, b):
            print("YES")
        else:
            print("NO")
