import sys
r = lambda: sys.stdin.readline().rstrip()

n, m = map(int, r().split(" "))
lst = []
result = []
for _ in range(n):
    lst.append(r())
lst = set(lst)

for _ in range(m):
    x = r()
    if x in lst:
        result.append(x)

result.sort()
print(len(result))
for i in result:
    print(i)