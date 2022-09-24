#code1 > 시간초과
import sys
r = sys.stdin.readline

N = int(r())
number = list(map(int, r().split()))
answer = number[0]

for i in range(N):
    now = number[i]
    for j in range(i+1, N):
        now += number[j]
        if now > answer:
            answer = now
        if now < 0:
            break
print(answer)

#code2
import sys
r = sys.stdin.readline

N = int(r())
number = list(map(int, r().split()))
answer = number[0]

lst = []
lst.append(number[0])
for i in range(1, len(number)):
    now = lst[-1] + number[i]
    lst.append(max(now, number[i]))
print(max(lst))
