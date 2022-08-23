''''
반복문을 사용한 이진 탐색 코드
''''

import sys 
r = sys.stdin.readline

n, target = map(int, r().split(" "))
lst = list(map(int, r().split(" ")))
start = 0
end = n-1

while True:
    if start>end:
        print("해당 값이 없습니다")
    mid = (start+end)//2
    if lst[mid] == target:
        print(mid+1)
    elif lst[mid]>target:
        end = mid-1
    else:
        start = mid+1
