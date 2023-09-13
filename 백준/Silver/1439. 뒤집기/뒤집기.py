import sys
import math
r = lambda: sys.stdin.readline().rstrip()

s = r()
cnt = 0
prev = s[0]
for i in range(1, len(s)):
    if prev != s[i]:
        cnt += 1
    prev = s[i]

print(math.ceil(float(cnt)/2.0))