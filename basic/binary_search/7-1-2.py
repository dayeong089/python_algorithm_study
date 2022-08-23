''''
계수 정렬을 활용한 코드
''''
#code1
import sys
r = sys.stdin.readline

n = int(r())
lst1 = list(map(int, r().split(" ")))
m = int(r())
lst2 = list(map(int, r().split(" ")))

min = min(lst1)
max = max(lst1)
length = max-min+1
lst = [0]*length

for i in range(len(lst1)):
    lst[lst1[i]-min] += 1

for i in range(len(lst2)):
    if lst[lst2[i]-min]!=0:
        print("yes", end=' ')
    else:
        print("no", end=' ')

#code2 - 더 간단하지만 메모리를 더 많이 차지함
import sys
r = sys.stdin.readline

n = int(r())
array = [0]*1000001

for i in r().split(" "):
    array[int(i)] = 1

m = int(r())
lst = list(map(int, r().split(" ")))

for i in lst:
    if array[i] == 1:
        print("yes", end=" ")
    else:
        print("no", end=" ")
