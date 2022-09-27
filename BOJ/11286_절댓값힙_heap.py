import sys
from heapq import heappush, heappop
r = sys.stdin.readline

n = int(r())
heap = []
for _ in range(n):
    x = int(r())
    if x == 0:
        if len(heap) != 0:
            now = heappop(heap)
            print(now[1])
        else:
            print("0")
    else:
        if x<0: x2 = -x
        else: x2 = x
        heappush(heap, (x2, x))
