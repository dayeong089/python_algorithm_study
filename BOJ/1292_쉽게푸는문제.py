import sys
r = sys.stdin.readline

lst = []
num = 1

while True:
    for i in range(num):
        lst.append(num)
    num+=1
    if len(lst)>1000:
        break

x, y = map(int, r().split(" "))
lst = lst[x-1:y]
print(sum(lst))
