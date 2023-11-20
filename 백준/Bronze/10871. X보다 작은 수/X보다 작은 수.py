N, X = map(int, input().split())

list = input().split()

for i in range(N):
    num = int(list[i])
    if num < X:
        print(num, end=" ")