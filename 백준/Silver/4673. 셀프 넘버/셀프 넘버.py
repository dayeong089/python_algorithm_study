num = list(range(1, 10001))
answer = []

for i in range(1, 10001):
    now = i
    while i>0:
        now += i%10
        i //= 10
    if now <= 10000:
        answer.append(now)

answer = set(answer)
for a in answer:
    num.remove(a)

for n in num:
    print(n)