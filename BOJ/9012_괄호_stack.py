import sys
r = sys.stdin.readline

n = int(r())

for _ in range(n):
    now = 0
    lst = list(r().rstrip())
    stack = []
    for i in lst:
        if i == "(":
            stack.append("(")
        else:
            if stack:
                stack.pop()
            else:
                print("NO")
                now = 1
                break

    if now == 0:
        if stack: print("NO")
        else: print("YES")
