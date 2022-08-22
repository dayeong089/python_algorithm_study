import sys
r = sys.stdin.readline

n = int(r())
lst = []
for i in range(n):
    x = int(r())
    lst.append(x)

lst.sort(reverse=True)

for i in lst:
    print(i, end=' ')
