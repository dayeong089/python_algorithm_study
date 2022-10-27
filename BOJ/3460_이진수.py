import sys
r = sys.stdin.readline

t = int(r())
for _ in range(t):
    n = int(r())
    num = 0
    lst = []
    while n>1:
        x = n%2
        if x == 1: lst.append(num)
        n//=2
        num+=1
    if n==1:
        lst.append(num)
    for i in lst:
        print(i, end=" ")
    print()
