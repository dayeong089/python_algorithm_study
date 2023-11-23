N, M = map(int, input().split(" "))
card = list(map(int, input().split()))
list = []

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            sum_value = card[i] + card[j] + card[k]
            if sum_value <= M:
                list.append(sum_value)

print(max(list))