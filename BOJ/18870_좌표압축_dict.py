# list index 함수 시간 복잡도 : O(N)
# dict 시간 복잡도 : O(1)

import sys
r = sys.stdin.readline

n = int(r())
lst = list(map(int, r().split(" ")))
lst2 = list(set(lst))
lst2.sort()

dict = {lst2[i] : i for i in range(len(lst2))}

for i in lst:
    print(dict[i], end=" ")
