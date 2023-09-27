import sys
r = sys.stdin.readline

n = int(r())
lst = [i for i in range(1, n+1)]
result_arr = []

while True:
    result_arr.append(lst[0])
    lst.pop(0)

    if len(lst) == 0:
        break

    lst.append(lst[0])
    if len(lst) == 1:
        result_arr.append(lst[0])
        break

    lst.pop(0)

for result in result_arr:
    print(result, end=" ")