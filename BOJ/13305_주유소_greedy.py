#code1 - min 함수 이용 > 시간초과
import sys
r = sys.stdin.readline

n = int(r())
road = list(map(int, r().split(" ")))
price = list(map(int, r().split(" ")))
result = 0

for i in range(len(road)):
    min_price = min(price[:i+1])
    result += (min_price * road[i])

print(result)

#code2
import sys
r = sys.stdin.readline

n = int(r())
road = list(map(int, r().split(" ")))
price = list(map(int, r().split(" ")))

result = road[0] * price[0]
min_price = price[0]
dist = 0

for i in range(1, n-1):
    if price[i] < min_price:
        min_price = price[i]
        result += (road[i] * min_price)
    else:
        result += (road[i] * min_price)

print(result)
