N, M = map(int, input().split(" "))
list = []
can1 = 0
can2 = 0
result = []
for i in range(N):
	list.append(input())
    
for i in range(N-7):
	for j in range(M-7):
		can1 = 0
		can2 = 0
		for x in range(i, i+8):
			for y in range(j, j+8):
				if x%2==y%2:
					if list[x][y] != 'B':
						can1 += 1
				else:
					if list[x][y] != 'W':
						can1 += 1		
		for x in range(i, i+8):
			for y in range(j, j+8):
				if x%2==y%2:
					if list[x][y] != 'W':
						can2 += 1
				else:
					if list[x][y] != 'B':
						can2 += 1
		result.append(min(can1, can2))
        
print(min(result))