#고치기 전 코드 
import sys
r = sys.stdin.readline

n = int(r())
lst = [[0]*n for _ in range(n)]
arr = []
for _ in range(n):
    x = list(map(int, r().split(" ")))
    arr.append(x)

lst[0][0] = arr[0][0]
for i in range(1, n):
    for j in range(i+1):
        if j==0:
            lst[i][j] = arr[i][j] + lst[i-1][j]
        elif j==i:
            lst[i][j] = arr[i][j] + lst[i-1][j-1]
        else:
            lst[i][j] = arr[i][j] + max(lst[i-1][j], lst[i-1][j-1])
print(max(lst[n-1]))

#수정된 코드 - 삼각형 정보 리스트, 합 리스트 굳이 분리하지 않아도 되므로 하나로 구현
import sys
r = sys.stdin.readline

n = int(r())
lst = []
for _ in range(n):
    lst.append(list(map(int, r().split(" "))))

for i in range(1, n):
    for j in range(i+1):
        if j==0:
            lst[i][0] = lst[i][0] + lst[i-1][0]
        elif j==i:
            lst[i][j] = lst[i][j] + lst[i-1][j-1]
        else:
            lst[i][j] = lst[i][j] + max(lst[i-1][j], lst[i-1][j-1])
print(max(lst[n-1]))
