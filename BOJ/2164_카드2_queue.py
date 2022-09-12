import sys
from collections import deque
r = sys.stdin.readline

n = int(r())
q = deque()

for i in range(1, n+1):
    q.append(i)

while len(q)!=1:
    q.popleft()
    x = q.popleft()
    q.append(x)

print(q[0])
