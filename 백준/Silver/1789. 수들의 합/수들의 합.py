import sys
r = sys.stdin.readline

n = int(r())
now = 0 #numvalue
num = 1 #minusvalue
cnt = 1 #count

while True:
    n -= num
    num += 1
    if n < num:
        break
    cnt += 1

print(cnt)