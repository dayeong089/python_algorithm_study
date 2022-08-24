import sys
r = sys.stdin.readline

n, m = map(int, r().split(" "))
coin = [int(r()) for _ in range(n)]

lst = [10001] * (m+1)
lst[0] = 0

for i in range(m+1):
    for j in coin:
        if i>=j and lst[i-j]!=10001:
            lst[i] = min(lst[i], lst[i-j]+1) 

if lst[i] == 10001:
    print("-1")
else:
    print(lst[i])
