import sys
r = sys.stdin.readline

n, m = map(int, r().split(" "))
lst = list(map(int, r().split(" ")))

start = 0
end = max(lst)
result = 0

while True:
    if start>end:
        break
    mid = (start+end)//2
    cnt = 0
    for x in lst:
        if x>mid:
            cnt += (x-mid)
    print(start, end, cnt)
    if cnt<m:
        end = mid-1
    else:
        result = mid
        start = mid+1

print(result)
