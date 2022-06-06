'''
<거스름돈>
거술러줘야 할 동전의 최소 개수를 구하라.
동전의 종류 : 500, 100, 50, 10
>> 가지고 있는 동전 중에서 큰 단위가 항상 작은 단위의 배수이므로 그리디 알고리즘 사용 가능
'''

from re import X
import sys
r = sys.stdin.readline

N = int(r())
coin_types = [500, 100, 50, 10]
cnt = 0

for coin in coin_types:
    x = N//coin
    cnt += x
    N %= coin

print(cnt)
