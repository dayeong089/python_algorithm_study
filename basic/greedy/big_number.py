'''
<큰 수의 법칙>
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
