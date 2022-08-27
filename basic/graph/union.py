# 서로소 집합 union 연산

import sys
r = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

def union_parent(parent, x, y):
    p1 = find_parent(parent, x)
    p2 = find_parent(parent, y)
    if p1 > p2:
        parent[p1] = p2
    else:
        parent[p2] = p1

v, e = map(int, r().split(" "))
parent = [i for i in range(v+1)]

for i in range(e):
    a, b = map(int, r().split(" "))
    union_parent(parent, a, b)

print("root parent:", end=" ")
for i in range(1, v+1):
    print(find_parent(parent, i), end=" ")
# print(find_parent(parent, i) for i in range(1, v+1))

print("parent table:", end=" ")
for i in range(1, v+1):
    print(parent[i], end=" ")
# print(parent[i] for i in range(1, v+1))
