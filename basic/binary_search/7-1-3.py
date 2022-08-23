''''
집합 자료형 사용하여 해결
''''

import sys
r = sys.stdin.readline

n = int(r())
lst = set(map(int, r().split(" "))) #set 대신 list를 사용 가능, 중복 제거하기 위해 set 사용?

m = int(r())
lst2 = list(map(int, r().split(" ")))

for i in lst2:
    if i in lst:
        print("yes", end=" ")
    else:
        print("no", end=" ")
