import sys
r = sys.stdin.readline

n = int(r())
lst = []
sumlst = [0]*n
for _ in range(n):
    x = int(r())
    lst.append(x)

sumlst[0] = lst[0]
if n>1:
    sumlst[1] = lst[0]+lst[1]
    if n>2:
        sumlst[2] = max(lst[0]+lst[1], lst[1]+lst[2], lst[0]+lst[2])
        if n>3:
            for i in range(3, n):
                now_lst = []
                now_lst.append(sumlst[i-3]+lst[i-1]+lst[i])
                now_lst.append(sumlst[i-2]+lst[i])
                now_lst.append(sumlst[i-1])
                sumlst[i] = max(now_lst)

print(sumlst[n-1])
