# list, rstrip, sort

import sys
r = sys.stdin.readline

lst = list(map(int, r().rstrip()))
lst.sort(reverse=True)
for i in lst:
    print(i, end="")
