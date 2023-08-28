import sys
r = sys.stdin.readline

stack = []
n = int(r())

for i in range(n):
    input = r().rstrip().split(" ")
    if len(input) == 2:
        stack.append(input[1])
    else:
        x = int(input[0])
        if x == 2:
            if len(stack) == 0: print("-1")
            else: 
                print(stack.pop())
        elif x == 3:
            print(len(stack))
        elif x == 4:
            if len(stack) == 0: print("1")
            else: print("0")
        elif x == 5:
            if len(stack) == 0: print("-1")
            else: print(stack[-1])