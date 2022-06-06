'''
<큰 수의 법칙>
다양한 수로 이루어진 배열이 있을 때, 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙을 구현하라.
배열의 특정한 번호에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없다.
input : N(배열의 크기), M, K
output : 만들 수 있는 가장 큰 수
>> 배열의 가장 큰 수와 두 번째로 큰 수만 사용
>> 반복문을 사용해서 풀 수도 있지만 시간초과가 발생하므로, 가장 큰 수 K개와 두 번째로 큰 수 1개로 이루어진 수열을 반복하여 더한다고 생각하여 반복문 없이 수학적 계산법으로 해결
'''
import sys
r = sys.stdin.readline

N, M, K = map(int, r().split(" "))
lst = list(map(int, r().split(" ")))

lst.sort(reverse = True)
num = 0

x = M//(K+1)
y = M%(K+1)
num += (lst[0]*K + lst[1])*x
num += lst[0]*y

print(num)
