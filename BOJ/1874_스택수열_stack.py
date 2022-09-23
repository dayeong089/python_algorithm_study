import sys
r = sys.stdin.readline

n = int(r())
stack = []
result = []
lst = []
for _ in range(n):
    x = int(r())
    lst.append(x)

num = 1
check = True
while lst:
    if len(stack)==0 or stack[-1]<lst[0]:
        result.append("+")
        stack.append(num)
        num += 1
    elif stack[-1]>lst[0]:
        print("NO")
        check = False
        break
    elif stack[-1]==lst[0]:
        result.append("-")
        lst.remove(lst[0])
        stack.pop()
        
if check == True:
    for i in result:
        print(i)
