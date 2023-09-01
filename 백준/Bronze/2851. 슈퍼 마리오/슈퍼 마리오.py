import sys
r = sys.stdin.readline

now = 0
diff = sys.maxsize
result = 0

for i in range(10):
    now += int(r())
    x = abs(now - 100)

    if diff > x:
        diff = x
        result = now

    elif diff == x:
        if now > result:
            result = now

print(result)