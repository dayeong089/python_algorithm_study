import sys
r = sys.stdin.readline

n, m = map(int, r().split(" "))
basket = [0] * n

for _ in range(m):
    i, j, k = map(int, r().split(" "))
    for x in range(i, j+1):
        basket[x-1] = k

for x in range(n):
    print(basket[x], end=' ')