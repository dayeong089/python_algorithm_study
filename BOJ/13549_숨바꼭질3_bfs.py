# 첫 코드
import sys
from collections import deque
r = sys.stdin.readline

n, k = map(int, r().split(" "))

if n==k:
    print(0)
    sys.exit()

if n>k:
    print(n-k)
    sys.exit()

visited = [False]*100001
loc_time = [-1]*100001

q = deque()
q.append((n, 0))

while q:
    if loc_time[k] != 0:
        check = True
        for i in q:
            if i[0] < k:
                check = False
                break
        if check:
            break

    loc, time = q.popleft()
    visited[loc] = True

    if loc*2 <= 100000:
        if loc_time[loc*2]==-1 or loc_time[loc*2]>time:
            q.append((loc*2, time))
            loc_time[loc*2] = time

    if loc-1 >= 0:
        if loc_time[loc-1]==-1 or loc_time[loc-1]>time+1:
            q.append((loc-1, time+1))
            loc_time[loc-1] = time+1

    if loc+1 <= 100000:
        if loc_time[loc+1]==-1 or loc_time[loc+1]>time+1:
            q.append((loc+1, time+1))
            loc_time[loc+1] = time+1

print(loc_time[k])

''''
순간이동은 0초로 시간이 추가되지 않기 때문에
loc == k인 시점이 나오더라도 그보다 짧은 시간으로 이동할 수 있는 방안이 그 후에 나올 수 있다고 생각
따라서 loc == k인 시점이 나오더라도 while문을 멈추지 않았음
하지만 순간이동을 이용해 더 짧은 시간으로 이동이 가능하다면 그보다 많은 시간을 요구하는 방안보다 빨리 queue에서 나올 것 > 따라서 while문 멈추면 됌
(상식적으로 2>1024할때 2>4>8>,,>1024 이런식으로 순간이동을 이용하는 것이 2>3>4... 이런식으로 이동하는 것보다 빨리 queue에서 pop될것임
...너무 어렵게 생각해서 코드가 더 복잡해진
''''

# 두번째 코드
import sys
from collections import deque
r = sys.stdin.readline

n, k = map(int, r().split(" "))

if n==k:
    print(0)
    sys.exit()

if n>k:
    print(n-k)
    sys.exit()

visited = [False]*100001
q = deque()
q.append((n, 0))

while q:
    loc, time = q.popleft()
    visited[loc] = True

    if loc == k:
        print(time)
        sys.exit()

    if loc*2 <= 100000 and visited[loc*2] == False:
        q.append((loc*2, time))
    
    if loc-1 >= 0 and visited[loc-1] == False:
        q.append((loc-1, time+1))

    if loc+1 <= 100000 and visited[loc+1] == False:
        q.append((loc+1, time+1))
