# bfs로 풀이
import sys
from collections import deque
r = sys.stdin.readline

a, b = map(int, r().split(" "))
result = 0

def bfs(a, b):
    global result
    q = deque()
    q.append((a, 1))

    while q:
        num, cnt = q.popleft()
        x1 = num*2
        x2 = num*10 + 1

        if x1 == b or x2 == b:
            print(cnt+1)
            result = cnt+1

        if x1<b:
            q.append((x1, cnt+1))
        if x2<b:
            q.append((x2, cnt+1))

bfs(a, b)
if result == 0:
    print("-1")

# 역으로 b에서 a를 구하는 방법
import sys

a, b= map(int,sys.stdin.readline().split())
cnt = 1
while(a<b):
  cnt += 1
  if b % 10 == 1:
    b = (b - 1) // 10
  elif b % 2 == 0:
    b = b //2
  else:
    break

if a == b:
  print(cnt)
else:
  print(-1)
