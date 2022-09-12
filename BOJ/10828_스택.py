import sys
r = sys.stdin.readline

n = int(r())
lst = []

for _ in range(n):
    x = r().rstrip()
    if "push" in x:
        x, y = x.split(" ")
        lst.append(y)
    if "pop" in x:
        if len(lst) == 0:
            print("-1")
        else:
            a = lst.pop()
            print(a)
    if "size" in x:
        print(len(lst))
    if "empty" in x:
        if len(lst) == 0:
            print("1")
        else:
            print("0")
    if "top" in x:
        if len(lst) == 0:
            print("-1")
        else:
            print(lst[-1])
