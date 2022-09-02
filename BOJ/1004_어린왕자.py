import sys
r = sys.stdin.readline

t = int(r())
result = []

for _ in range(t):
    x1, y1, x2, y2 = map(int, r().split(" "))
    n = int(r())
    cnt = 0
    for _ in range(n):
        x3, y3, rad = map(int, r().split(" "))
        d1 = (x1-x3)*(x1-x3) + (y1-y3)*(y1-y3)
        d2 = (x2-x3)*(x2-x3) + (y2-y3)*(y2-y3)
        d3 = rad*rad

        if d1 < d3 and d2 >= d3 or d2 < d3 and d1 >= d3:
            cnt += 1
            
    result.append(cnt)

for i in result:
    print(i)
