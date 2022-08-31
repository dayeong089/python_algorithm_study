# list 중복 없애기 > lst = list(set(lst))
# lambda 활용

# 풀이1
import sys
r = sys.stdin.readline

n = int(r())
lst = [[] for _ in range(51)]

for _ in range(n):
    x = r().rstrip()
    x_len = len(x)
    lst[x_len].append(x)

for i in range(len(lst)):
    lst[i] = list(set(lst[i]))
    lst[i].sort()

for i in lst:
    if len(i) != 0:
        for j in i:
            print(j)
            
# 풀이2 - lambda 활용
import sys
r = sys.stdin.readline

n = int(r())
lst = []
for _ in range(n):
    x = r().rstrip()
    lst.append(x)

lst = list(set(lst))

lst.sort()
lst.sort(key = lambda x : len(x))

for i in lst:
    print(i)
