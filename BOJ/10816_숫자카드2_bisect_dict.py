# bisect 이용
import sys
from bisect import bisect_left, bisect_right
r = sys.stdin.readline

def count_num(lst, left, right):
    x1 = bisect_left(lst, left)
    x2 = bisect_right(lst, right)
    result = x2 - x1
    return result

n = int(r())
lst = list(map(int, r().split(" ")))
lst.sort()

m = int(r())
lst2 = list(map(int, r().split(" ")))

for i in lst2:
    print(count_num(lst, i, i), end=" ")

# dict 이용
import sys
r = sys.stdin.readline

n = int(r())
lst = list(map(int, r().split(" ")))
m = int(r())
lst2 = list(map(int, r().split(" ")))
count = {}

for i in lst:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

for i in lst2:
    if i in count:
        print(count[i], end=' ')
    else:
        print(0, end=' ')
