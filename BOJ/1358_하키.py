import sys
r = sys.stdin.readline

w, h, x, y, p = map(int, r().split(" "))
player = []
cnt = 0

for _ in range(p):
    a, b = map(int, r().split(" "))
    x1 = x + w
    y1 = y + (h/2)
    d1 = (a-x)*(a-x) + (b-y1)*(b-y1)
    d2 = (a-x1)*(a-x1) + (b-y1)*(b-y1)
    d3 = (h/2)*(h/2)

    if a >= x and a <= x+w and b >= y and b <= y+h:
        cnt += 1
    elif d1 <= d3 or d2 <= d3:
        cnt += 1

print(cnt)
