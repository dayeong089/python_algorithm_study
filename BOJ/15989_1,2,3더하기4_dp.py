# 첫번째 코드 - 덧셈 공식에 1이 포함된 경우, 1이 없는 경우, 1,2 모두 없는 경우로 나눠서 생각
import sys
r = sys.stdin.readline

t = int(r())
lst = [[0]*3 for _ in range(10001)]

lst[1] = [1, 0, 0]
lst[2] = [1, 1, 0]
lst[3] = [2, 0, 1]

for i in range(4, 10001):
    lst[i][0] = sum(lst[i-1]) 
    lst[i][1] = lst[i-2][1] + lst[i-2][2]
    lst[i][2] = lst[i-3][2]

for _ in range(t):
    x = int(r())
    print(sum(lst[x])) 
    
# 두번째 코드
import sys
r = sys.stdin.readline

t = int(r())
lst = [1]*10001 #1로만 이루어진 경우

for i in range(2, 10001):
    lst[i] += lst[i-2] #1,2로 이루어진 경우

for i in range(3, 10001):
    lst[i] += lst[i-3] #1,2,3

for _ in range(t):
    x = int(r())
    print(lst[x])
