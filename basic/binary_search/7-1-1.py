''''
이진 탐색을 활용한 코드
시간 복잡도 : O((M+N)logN)
''''

import sys
r = sys.stdin.readline

def binary_search(lst, start, end, target):
    if start>end:
        print("no", end=' ')
        return
    mid=(start+end)//2
    if lst[mid]==target:
        print("yes", end=' ')
        return
    elif lst[mid]>target:
        binary_search(lst, start, mid-1, target)
    else:
        binary_search(lst, mid+1, end, target)

n = int(r())
lst = list(map(int, r().split(" ")))
lst.sort()
m = int(r())
lst2 = list(map(int, r().split(" ")))

for i in range(len(lst2)):
    target=lst2[i]
    binary_search(lst, 0, len(lst)-1, target)
