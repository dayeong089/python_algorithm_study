N = int(input())
result = 0

if N < 100:
    result = N
else:
    result = 99
    for i in range(100, N+1):
        if i <= 999:
            x = i%10 - (i//10)%10
            y = (i//10)%10 - (i//100)%10
            if x == y:
                result += 1

print(result)
    