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
