import sys
r = lambda: sys.stdin.readline().rstrip()

n = int(r())
arr = [[0]*101 for _ in range(101)]
for i in range(n):
    x, y = map(int, r().split(" "))
    for i in range(10):
        for j in range(10):
            arr[x+i][y+j] = 1

result = 0
for i in arr:
    result += sum(i)

print(result)