# set을 사용하여 방문 
import sys
from collections import deque
r = sys.stdin.readline

n, k = map(int, r().split(" "))
lst = set()

def bfs(n, k):
    if n == k:
        print(0)
        return
    if n > k:
        print(n-k)
        return

    q = deque()
    q.append((n, 0))
    while q:
        loc, time = q.popleft()
        now = time+1
        loc1 = loc+1
        loc2 = loc-1
        loc3 = loc*2

        if 0<=loc1<=100000 and loc1 not in lst: 
            lst.add(loc1)
            if loc1==k:
                print(now)
                return
            else:
                q.append((loc1, now))
                
        if 0<=loc2<=100000 and loc2 not in lst:
            lst.add(loc2)
            if loc2==k:
                print(now)
                return
            else:
                q.append((loc2, now))
                
        if 0<=loc3<=100000 and loc3 not in lst:
            lst.add(loc3)
            if loc3==k:
                print(now)
                return
            else:
                q.append((loc3, now))
        
bfs(n, k)


# 다른 풀이 - visited list 사용해서 방문 체크
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

visited = [False]*200001

q = deque()
q.append((n, 0))
visited[n] = True

while q:
    loc, time = q.popleft()
    lst = [loc-1, loc+1, loc*2]
    for i in lst:
        if i == k:
            print(time+1)
            sys.exit()
        if 0<=i<=200000:
            if visited[i]==False:
                q.append((i, time+1))
                visited[i] = True
