import sys
r = sys.stdin.readline

stack = []
n = int(r())

for i in range(n):
    input = r().rstrip().split(" ")
    
    if input[0] == '1':
        stack.append(input[1])
    elif input[0] == '2':
        if stack: print(stack.pop())
        else: print("-1")
    elif input[0] == '3':
        print(len(stack))
    elif input[0] == '4':
        if stack: print("0")
        else: print("1")
    elif input[0] == '5':
        if stack: print(stack[-1])
        else: print("-1")