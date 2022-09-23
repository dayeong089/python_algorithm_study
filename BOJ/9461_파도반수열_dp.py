import sys
r = sys.stdin.readline
t = int(r())
lst = [0] * 101
lst[1] = 1
lst[2] = 1
lst[3] = 1

for _ in range(t):
    n = int(r())
    for i in range(3, n+1):
        lst[i] = lst[i-2] + lst[i-3]
    print(lst[n])
