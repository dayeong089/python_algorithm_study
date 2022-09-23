#code1 > 리스트에 모든 경우에 대한 값 저장
import sys
r = sys.stdin.readline
INF = 1e9
lst = []
for _ in range(101):
    now1 = []
    for _ in range(101):
        now2 = [INF] * 101
        now1.append(now2)
    lst.append(now1)

def w(a, b, c):
    if lst[a+50][b+50][c+50] != INF:
        return lst[a+50][b+50][c+50]
    elif a<=0 or b<=0 or c<=0:
        lst[a+50][b+50][c+50] = 1
    elif a>20 or b>20 or c>20:
        lst[a+50][b+50][c+50] = w(20, 20, 20)
    elif a<b<c:
        lst[a+50][b+50][c+50] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    else:
        lst[a+50][b+50][c+50] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    return lst[a+50][b+50][c+50]

a, b, c = map(int, r().split(" "))
while True:
    if a==-1 and b==-1 and c==-1:
        break
    result = w(a, b, c)
    print("w(%d, %d, %d) = %d" %(a, b, c, result))
    a, b, c = map(int, r().split(" "))
    
#code2 > 0~20에 대한 경우만 저장
import sys
r = sys.stdin.readline
INF = 1e9
lst = [[[INF]*21 for _ in range(21)] for __ in range(21)]

def w(a, b, c):
    if a<=0 or b<=0 or c<=0:
        return 1
    elif a>20 or b>20 or c>20:
        return w(20, 20, 20)
    elif lst[a][b][c] != INF:
        return lst[a][b][c]
    elif a<b<c:
        lst[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    else:
        lst[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    return lst[a][b][c]

a, b, c = map(int, r().split(" "))
while True:
    if a==-1 and b==-1 and c==-1:
        break
    result = w(a, b, c)
    print("w(%d, %d, %d) = %d" %(a, b, c, result))
    a, b, c = map(int, r().split(" "))
