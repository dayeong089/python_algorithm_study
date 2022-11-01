# 첫 코드 - case 따로 작성, 매번 stack 빈 여부 체크해서 복잡
import sys
r = sys.stdin.readline

lst = list(r().rstrip())
stack = []
check = True

for i in lst:
    if i == "(" or i == "[":
        stack.append(i)
    elif i == ")":
        if len(stack) == 0:
            check = False
            break
        else:
            if stack[-1] == "(":
                stack.pop()
                stack.append(2)
            elif stack[-1]!=")" and stack[-1]!="[" and stack[-1]!="]":
                num = 0
                while True:
                    num += stack[-1]
                    stack.pop()
                    if len(stack) == 0:
                        check = False
                        break
                    else:
                        if stack[-1] == "(":
                            stack.pop()
                            stack.append(num*2)
                            break
                        elif stack[-1] == "[" or stack[-1] == "]":
                            check = False
                            break
            else:
                check = False
                break
    elif i == "]":
        if len(stack) == 0:
            check = False
            break
        else:
            if stack[-1] == "[":
                stack.pop()
                stack.append(3)
            elif stack[-1]!="]" and stack[-1]!="(" and stack[-1]!=")":
                num = 0
                while True:
                    num += stack[-1]
                    stack.pop()
                    if len(stack) == 0:
                        check = False
                        break
                    else:
                        if stack[-1] == "[":
                            stack.pop()
                            stack.append(num*3)
                            break
                        elif stack[-1] == "(" or stack[-1] == ")":
                            check = False
                            break
            else:
                check = False
                break
    if check == False:
        break

for i in stack:
    if i == "(" or i == ")" or i == "[" or i == "]":
        check = False

if check == True:
    print(sum(stack))
else:
    print("0")
    
# 두번째 코드 - dict 사용, 성립 안되는 경우 미리 체크해서 코드 단축
import sys
r = sys.stdin.readline

lst = list(r().rstrip())
stack = []
di = {")" : ("(", 2), "]" : ("[", 3)}
lst2 = ["(", ")", "[", "]"]
check = True

for i in lst:
    if i not in di:
        stack.append(i)
    else:
        if stack and stack[-1] == di[i][0]:
            stack.pop()
        else:
            stack.append(i)
if stack:
    print(0)
    sys.exit(0)

for i in lst:
    if i not in di:
        stack.append(i)
    else:
        if stack[-1] == di[i][0]:
            stack.pop()
            stack.append(di[i][1])
        else:
            num = stack[-1]*di[i][1]
            stack.pop()
            stack.pop()
            stack.append(num)
        if len(stack)>1 and stack[-2] not in lst2:
            num = stack[-1] + stack[-2]
            stack.pop()
            stack.pop()
            stack.append(num)

print(sum(stack))

# 마지막 부분 이렇게 수정할 수 있음
        else:
            num = stack[-1]*di[i][1]
            stack.pop()
            stack.pop()
            stack.append(num)
        if len(stack)>1 and stack[-2] not in lst2:
            num = stack[-1] + stack[-2]
            stack.pop()
            stack.pop()
            stack.append(num)
  
  
         else:
            v = 0
            while tmp != dict[e][1]:
                v += tmp
                tmp = stack.pop()
            stack.append(v * dict[e][0])
