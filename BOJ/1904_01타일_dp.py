#code1
import sys
r = sys.stdin.readline

n = int(r())
lst = [0] * 1000001
lst[1] = 1
lst[2] = 2

for i in range(3, n+1):
    lst[i] = (lst[i-1] + lst[i-2]) % 15746

print(lst[n])

#code2 > 메모리, 시간 효율도 높이기
import sys
r = sys.stdin.readline

n = int(r())
a = 1
b = 2
c = 3
for i in range(3, n+1):
    c = (a+b)%15746
    a = b
    b = c

if n==1: print(1)
elif n==2: print(2)
else: print(c)
