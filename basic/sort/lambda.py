import sys
r = sys.stdin.readline

n = int(r())
lst = []

for i in range(n):
    x, y = r().split(" ")
    lst.append((x, int(y)))

lst.sort(key=lambda x:x[1])

for i in lst:
    print(i[0], end=" ")
    
''''
<key=lambda x:y>에서 x가 입력(리스트의 원소), y가 출력이 되서 정렬할 때 y값이 정렬의 기준이 된다
''''
