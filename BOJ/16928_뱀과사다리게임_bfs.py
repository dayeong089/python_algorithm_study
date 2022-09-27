import sys
from collections import deque
r = sys.stdin.readline

n, m = map(int, r().split(" "))
lst = [0] * 101
ladder = []
snake = []

for _ in range(n):
    x, y = map(int, r().split(" "))
    ladder.append((x, y))
for _ in range(m):
    x, y = map(int, r().split(" "))
    snake.append((x, y))

q = deque()
q.append((1, 0))
while q:
    loc, num = q.popleft()
    check = True
    for i in ladder:
        if loc == i[0]:
            now = i[1]
            lst[now] = num
            q.append((now, num))
            check = False
    for i in snake:
        if loc == i[0]:
            now = i[1]
            lst[now] = num
            q.append((now, num))
            check = False
    if check == True: #현재 위치에 사다리나 뱀이 있으면 무조건 이동해야 함 > 그 위치에서 주사위 굴릴 수 없음
        for i in range(1, 7):
            now = loc+i
            if 1<=now<=100:
                if lst[now] == 0 or lst[now] > num+1:
                    lst[now] = num+1
                    q.append((now, num+1))
print(lst[100])

# graph에 갈 수 있는 위치 저장해서 푸는 방법도 있음
# 대략 이런식으로....
# graph = [[] for _ in range(100)]

# for i in range(100):
# 	for j in range(1,7):
# 		if i+j < 100:
# 			graph[i].append(i+j)

# for _ in range(n+m):
# 	x, y = map(int, input().split(" "))
# 	x-=1
# 	y-=1
# 	for line in graph:
# 		for i in range(len(line)):
# 			if line[i] == x:
# 				line[i] = y
