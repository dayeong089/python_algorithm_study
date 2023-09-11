N = int(input())
num = 0
cnt = 0
while N > 0:
    if N >= 5 and N % 5 == 0:
        num += (N//5)
        num += cnt
        break
    else:
        N -= 3
        cnt += 1
if N % 3 == 0 and num == 0:
    num += cnt
if num == 0:
    num = -1
print(num)