import sys
from collections import deque
r = sys.stdin.readline

dx = [2, 2, -2, -2, 1, 1, -1, -1]
dy = [1, -1, 1, -1, 2, -2, 2, -2]
result = []

def bfs(x, y, l, x1, y1):
    if x==x1 and y==y1:
        result.append(0)
        return

    q = deque()
    q.append((x, y, 0))
    lst = set()

    while q:
        x, y, num = q.popleft()
        for i in range(8):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<l and 0<=ny<l and (nx, ny) not in lst:
                if nx==x1 and ny==y1:
                    result.append(num+1)
                    return
                q.append((nx, ny, num+1))
                lst.add((nx, ny))

n = int(r())
for _ in range(n):
    l = int(r())
    x, y = map(int, r().split(" "))
    x1, y1 = map(int, r().split(" "))
    bfs(x, y, l, x1, y1)

for i in result:
    print(i)
