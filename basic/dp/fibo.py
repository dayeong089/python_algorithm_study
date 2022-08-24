#일반적 fibonacci 함수 코드
def fibo(x):
    if x == 1 or x == 2:
        return 1
    else:
        return fibo(x-1) + fibo(x-2)

print(fibo(100))


#Top-down 방식
lst = [0] * 101

def fibo(x):
    if x==1 or x==2:
        return 1
    if lst[x]!=0:
        return lst[x]
    else:
        lst[x]=fibo(x-1)+fibo(x-2)
        return lst[x]

print(fibo(100))


#Bottom-up 방식
lst = [0] * 101

lst[1] = 1
lst[2] = 1

n = 100
for i in range(3, n+1):
    lst[i] = lst[i-1] + lst[i-2]

print(lst[n])
