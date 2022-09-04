''''
list에서 x in s의 평균 시간복잡도 : O(n)
set에서 x in s의 평균 시간복잡도 : O(1) > 파이썬에서는 set가 hash table로 구현되어 있기 때문
remove 연산도 마찬가지
따라서 중복된 값이 없는 경우 list 대신 set를 이용하는 것이 효율적
''''

import sys
r = sys.stdin.readline

n = int(r())
lst = set(map(int, r().split(" ")))

m = int(r())
lst2 = list(map(int, r().split(" ")))

for i in lst2:
    if i in lst:
        print("1", end=" ")
    else:
        print("0", end=" ")
