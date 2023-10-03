N = int(input())
weight = []
height = []
result = []
for i in range(N):
	x, y = map(int, input().split(" "))
	weight.append(x)
	height.append(y)
	
for i in range(N):
	now_weight = weight[i]
	now_height = height[i]
	cnt = 1
	for j in range(N):
		if weight[j] > now_weight and height[j] > now_height:
			cnt += 1
	result.append(cnt)
	
for i in range(N):
	print(result[i], end=" ") 