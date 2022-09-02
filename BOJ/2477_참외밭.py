import sys
r = sys.stdin.readline

k = int(r())
lst = []

for _ in range(6):
    a, b = map(int, r().split(" "))
    lst.append((a, b))

max1 = 0
max2 = 0
idx1 = 0
idx2 = 0
for i in range(6):
    if lst[i][0] == 1 or lst[i][0] == 2:
        if lst[i][1] > max1:
            max1 = lst[i][1]
            idx1 = i
    elif lst[i][0] == 3 or lst[i][0] == 4:
        if lst[i][1] > max2:
            max2 = lst[i][1]
            idx2 = i

now1 = lst[(idx1+3)%6][1]
now2 = lst[(idx2+3)%6][1]

print((max1*max2 - now1*now2)*k)
