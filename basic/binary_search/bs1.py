''''
재귀 함수를 이용한 이진 탐색 코드
''''

import sys
r = sys.stdin.readline

def binary_search(lst, start, end, target):
    if start > end:
        return None

    mid = (start+end)//2
    if lst[mid] == target:
        return mid
    elif lst[mid] > target:
        return binary_search(lst, start, mid-1, target)
    else:
        return binary_search(lst, mid+1, end, target)

n, target = map(int, r().split(" "))
lst = list(map(int, r().split(" ")))

result = binary_search(lst, 0, n-1, target)
if result == None:
    print("해당 값이 없습니다")
else:
    print(result+1)
