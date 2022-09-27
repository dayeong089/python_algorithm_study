import sys
from heapq import heappop, heappush
r = sys.stdin.readline

n = int(r())
heap = []
for _ in range(n):
    x = int(r())
    if x == 0:
        if len(heap) == 0:
            print("0")
        else:
            now = heappop(heap)
            print(-now)
    else:
        heappush(heap, -x)
