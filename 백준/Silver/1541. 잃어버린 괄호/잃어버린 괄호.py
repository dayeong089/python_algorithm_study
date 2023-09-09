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