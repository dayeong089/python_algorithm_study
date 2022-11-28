#첫번째 풀이 - 시작부터 목적지까지의 경로를 q에 일일이 저장하여 프린트 > 시간이 매우 오래 걸림
import sys
from collections import deque
r = sys.stdin.readline

n, k = map(int, r().split(" "))

if n==k:
    print(0)
    print(n)
    sys.exit()

if n>k:
    print(n-k)
    for i in range(n, k-1, -1):
        print(i, end=" ")
    sys.exit()

visited = [False]*100001

q = deque()
q.append((n, 0, [n]))
visited[n] = True

while q:
    loc, time, lst = q.popleft()
    if loc == k:
        print(time)
        for i in lst:
            print(i, end=" ")
        break

    p = [loc+1, loc-1, loc*2]
    for i in p:
        if 0<=i<=100000 and visited[i]==False:
            lst2 = lst[:]
            lst2.append(i)
            q.append((i, time+1, lst2))
            visited[i] = True

#두번째 풀이 - 이전에 방문한 루트 한 곳만 리스트에 따로 저장 > 루트를 타고 타고 이동하며 경로를 프린트 > 시간 단축
import sys
from collections import deque
r = sys.stdin.readline

n, k = map(int, r().split(" "))
visited = [False]*100001
route = [0]*100001

if n==k:
    print(0)
    print(n)
    sys.exit()

if n>k:
    print(n-k)
    for i in range(n, k-1, -1):
        print(i, end=" ")
    sys.exit()

q = deque()
q.append((n, 0))
visited[n] = True

while q:
    loc, time = q.popleft()
    if loc == k:
        print(time)
        arr = [loc]
        for i in range(time):
            loc = route[loc]
            arr.append(loc)
        for i in range(len(arr)-1, -1, -1):
            print(arr[i], end=" ")

    lst = [loc+1, loc-1, loc*2]
    for i in lst:
        if 0<=i<=100000 and visited[i]==False:
            q.append((i, time+1))
            visited[i] = True
            route[i] = loc
