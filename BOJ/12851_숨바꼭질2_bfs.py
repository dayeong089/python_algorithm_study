import sys
from collections import deque
r = sys.stdin.readline

n, k = map(int, r().split(" "))
if n==k:
    print(0)
    print(1)
    sys.exit()
if n>k:
    print(n-k)
    print(1)
    sys.exit()

visited = [False]*100001
cnt = 0
min_time = 0

q = deque()
q.append((n, 0))

while q:
    loc, time = q.popleft()
    visited[loc] = True
    if loc == k:
        if cnt == 0:
            min_time = time # 최소 시간을 구해줌 - min_time
        cnt += 1 # 최소 시간으로 갈 수 있는 방법 수 - cnt
    if cnt!=0 and time > min_time: # time이 최소 시간을 넘기면 
        print(min_time)
        print(cnt)
        sys.exit()
    lst = [loc-1, loc+1, loc*2]
    for i in lst:
        if 0<=i<=100000:
            if visited[i]==False:
                q.append((i, time+1))
