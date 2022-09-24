import sys
r = sys.stdin.readline

n = int(r())
lst = []
sumlst = [0]*n
for _ in range(n):
    lst.append(int(r()))

sumlst[0] = lst[0]
if n>1:
    sumlst[1] = lst[0] + lst[1]
    if n>2:
        sumlst[2] = max(lst[0] + lst[2], lst[1] + lst[2])
        if n>3:
            for i in range(3, n):
                sumlst[i] = max(sumlst[i-3]+lst[i-1]+lst[i], sumlst[i-2]+lst[i])
print(sumlst[n-1])
