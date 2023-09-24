import sys
r = sys.stdin.readline

lst = []
k = int(r())
for _ in range(k):
    x = int(r())
    if x==0:
        lst.pop()
    else:
        lst.append(x)

print(sum(lst))