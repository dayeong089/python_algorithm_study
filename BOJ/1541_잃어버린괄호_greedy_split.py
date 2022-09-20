# code1-복잡
import sys
r = sys.stdin.readline

lst = list(r().rstrip())
num = []
oper = []
now = []

for i in lst:
    if i.isdigit():
        now.append(i)
    else:
        oper.append(i)
        now_num = 0
        for j in range(len(now)):
            now_num += int(now[j]) * (10**(len(now)-j-1))
        num.append(now_num)
        now = []

now_num = 0
for j in range(len(now)):
    now_num += int(now[j]) * (10**(len(now)-j-1))
num.append(now_num)

check = len(oper)
for i in range(len(oper)):
    if oper[i] == '-':
        check = i
        break

result = num[0]
for i in range(1, len(num)):
    if i <= check:
        result += num[i]
    else:
        result -= num[i]
print(result)

# code2-split 사용하여 간단하게 풀이
import sys
r = sys.stdin.readline

exp = r().rstrip().split("-")
result = 0

lst1 = exp[0].split("+")
for i in lst1:
    result += int(i)
    
for i in exp[1:]:
    lst2 = i.split("+")
    for j in lst2:
        result -= int(j)
print(result)
