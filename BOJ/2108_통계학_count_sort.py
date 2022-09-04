# 정렬, list count, index, sum, round 함수 활용

import sys
r = sys.stdin.readline

n = int(r())
lst = []
cnt = [0]*8001
for _ in range(n):
    x = int(r())
    lst.append(x)
    cnt[x+4000] += 1
lst.sort()

average = round(sum(lst)/n)
print(average)

mid = n//2
print(lst[mid])

freq_value = max(cnt)
freq_num = cnt.count(freq_value)
if freq_num == 1:
    print(cnt.index(freq_value)-4000)
else:
    first_idx = cnt.index(freq_value)
    cnt[first_idx] -= 1
    print(cnt.index(freq_value)-4000)

print(max(lst)-min(lst))
