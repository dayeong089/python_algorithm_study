import sys
r = sys.stdin.readline

n = int(r())
lst = list(map(int, r().split(" ")))
con = [1]*n

for i in range(1, n):
    biglst = []
    for j in range(i):
        if lst[j] > lst[i]:
            biglst.append(con[j])
    if len(biglst)!=0:
        con[i] = max(biglst)+1

print(max(con))
