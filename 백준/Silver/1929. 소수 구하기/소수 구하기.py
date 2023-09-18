import math
M, N = map(int, input().split(" "))
prime = [True] * (N+1)
prime[0] = False
prime[1] = False
k = int(math.sqrt(N))

for i in range(2, k+1):
    if prime[i] == True:
        for j in range(i+i, N+1, i):
            prime[j] = False

for i in range(M, len(prime)):
    if prime[i] == True:
        print(i)