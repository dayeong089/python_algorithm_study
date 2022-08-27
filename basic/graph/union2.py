# 서로소 집합 union 연산(2) - 경로 압축 기법 적용

import sys
r = sys.stdin.readline

def find_parent(parent, x):
    if parent[x]!=x:
        parent[x]=find_parent(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    x = find_parent(parent, x)
    y = find_parent(parent, y)
    if x > y:
        parent[x] = y
    else:
        parent[y] = x

v, e = map(int, r().split(" "))
parent = [i for i in range(v+1)]

for _ in range(e):
    a, b = map(int, r().split(" "))
    union(parent, a, b)

print("root parent :", end=" ")
for i in range(1, v+1):
    print(find_parent(parent, i), end=" ")

print("parent table :", end=" ")
for i in range(1, v+1):
    print(parent[i], end=" ")
