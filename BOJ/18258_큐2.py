import sys
from collections import deque
r = sys.stdin.readline

n = int(r())
queue = deque()

for _ in range(n):
    x = r().rstrip().split(" ")
    order = x[0]
    if order == "push":
        queue.append(x[1])
    elif order == "pop":
        if queue: print(queue.popleft())
        else: print("-1")
    elif order == "size":
        print(len(queue))
    elif order == "empty":
        if queue: print("0")
        else: print("1")
    elif order == "front":
        if queue: print(queue[0])
        else: print("-1")
    elif order == "back":
        if queue: print(queue[-1])
        else: print("-1")
