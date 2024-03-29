# stack 문제인데 string 다루는 아이디어 생각하는 것이 더 복잡했음

import sys
r = sys.stdin.readline

sent = ""
# 마지막에 . 들어올때까지 입력받음 + 하나의 문장으로 합침
while True:
    x = r().rstrip()
    sent += x 
    if sent[len(sent)-2:] == ".." or sent == ".":
        break

# 합친 문장을 .를 기준으로 나눠줌
sent_lst = sent.split(".")
sent_lst = sent_lst[:len(sent_lst)-2]

# 균형 잡힌 문장인지 검사
for j in sent_lst:
    now = 0
    lst = list(j)
    stack = []
    for i in lst:
        if i == "(" or i == "[":
            stack.append(i)
        elif i == ")":
            if stack:
                a = stack.pop()
                if a != "(":
                    print("no")
                    now = 1
            else:
                print("no")
                now = 1
        elif i == "]":
            if stack:
                a = stack.pop()
                if a != "[":
                    print("no")
                    now = 1
            else:
                print("no")
                now = 1
        if now == 1:
            break
    if now == 0:
        if stack: print("no")
        else: print("yes")
