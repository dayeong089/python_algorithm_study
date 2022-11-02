# 첫번째 - 연산자 순열 이용, 같은 경우를 제외하기 위해 list를 set으로 변환
import sys
from itertools import permutations
r = sys.stdin.readline

n = int(r())
num_lst = list(map(int, r().split(" ")))
oper_lst = list(map(int, r().split(" ")))
result = []

str = ""
for i in range(oper_lst[0]):
    str+="+"
for i in range(oper_lst[1]):
    str+='-'
for i in range(oper_lst[2]):
    str+="*"
for i in range(oper_lst[3]):
    str+='/'

olst = set(list(permutations(str, len(str))))

def cal(n1, n2, oper):
    if oper == "+":
        return n1+n2
    elif oper == "-":
        return n1-n2
    elif oper == "*":
        return n1*n2
    else:
        if n1<0 and n2>0:
            return(-(-n1//n2))
        else: return n1//n2

for i in olst:
    tmp = num_lst[0]
    for j in range(len(num_lst)-1):
        n1 = tmp
        n2 = num_lst[j+1]
        tmp = cal(n1, n2, i[j])
    result.append(tmp)

print(max(result))
print(min(result))
