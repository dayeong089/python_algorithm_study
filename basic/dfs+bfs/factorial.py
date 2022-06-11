# 팩토리얼 반복적으로 구현

n = 10
x = 1
for i in range(1, n+1):
    x *= i
    print(x)

print(x)

# 팩토리얼 재귀로 구현

def factorial(i):
    if i==1:
        return 1
    return factorial(i-1) * i

factorial(10)
