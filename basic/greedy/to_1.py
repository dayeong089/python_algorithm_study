'''
<1이 될 때까지>
어떠한 수 N이 1이 될 때 까지 다음의 두 과정 중 하나를 반복적으로 선택해 수행하려 함
단, 두번째 연산은 N이 K로 나누어 떨어질 때만 선택할 수 있음
1. N에서 1을 뺀다.
2. N을 K로 나눈다.
N이 1이 될 때 까지 1번 혹은 2번의 과정을 수행해야하는 최소 횟수를 구하는 프로그램을 작성

-input-
첫째 줄에 N(2<= N <= 100000)과 K(2 <= K <= 100000)가 공백으로 구분되며 각각 자연수로 주어짐
이때, 입력으로 주어지는 N은 항상 K보다 크거나 같음
-output-
첫째 줄에 N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야 하는 횟수의 최솟값을 출력

>> 첫번째 풀이 : N이 K로 나누어 떨어질 때까지 1씩 뺀다(1번 연산법), 나누어 떨어지면 나눈다(2번 연산법)
: 문제를 해결할 수는 있으나, N이 100억 이상의 큰 수가 된다고 가정하면 시간초과가 발생할 수도 있음
>> 두번째 풀이 : N을 K로 나누어 떨어지는 target 값으로 조정, 결과값에 (N-target)만큼 더해준다. 그 후 N을 K로 나누고 이를 반복한다.
: N이 K로 나누어 떨어질 때까지 1씩 빼는 것이 아니라 바로 나누어 떨어지는 값으로 조정하기 때문에 시간을 훨씬 절약할 수 있음.

'''
# 첫번째 풀이
import sys
r = sys.stdin.readline

N, K = map(int, r().split(" "))
cnt = 0
while True:
    if N%K != 0:
        N -= 1
    else:
        N //= K
    cnt += 1

    if N == 1:
        break

print(cnt)

# 두번째 풀이
import sys
r = sys.stdin.readline

N, K = map(int, r().split(" "))
cnt = 0

while True:
    target = (N//K) * K
    cnt += (N-target)
    N = target

    if N<K:
        break

    N //= K
    cnt += 1

cnt += (N-1)

print(cnt)
