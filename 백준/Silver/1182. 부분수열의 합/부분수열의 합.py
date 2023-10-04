from itertools import combinations

N, S = map(int, input().split(" "))
num = list(map(int, input().split(" ")))
cnt = 0

for i in range(1, N+1):
    com = list(combinations(num, i))
    for j in com:
        if sum(j) == S:
            cnt+=1
print(cnt)