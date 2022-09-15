# queue rotate
import sys
from collections import deque
r = sys.stdin.readline

n, k = map(int, r().split(" "))
q = deque(list(range(1,n+1)))
result = []

while q:
    for i in range(1, k+1):
        x = q.popleft()
        if i != k:
            q.append(x)
        else:
            result.append(x)

print('<', end='')
for i in range(n-1):
    print(result[i], end=', ')
print(result[n-1], end='')
print('>')
