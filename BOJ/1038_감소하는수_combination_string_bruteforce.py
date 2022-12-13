# 처음 풀이 : 차례대로 검사 후 감소하는 수가 아닌 경우 다음 감소하는 수로 jump
import sys
r = sys.stdin.readline

n = int(r())
cnt = -1 # 몇 번째?
num = 0 # 수

while True:
    lst = list(map(int, str(num)))

    check = True
    for i in range(len(lst)-1):
        if lst[i+1] >= lst[i]:
            check = False

            lst[i] += 1
            if lst[i] == 10:
                x = 1
                for j in range(len(lst)-1, i-1, -1):
                    lst[j] = x
                    x += 1
                lst.append(0)
            else:
                x = 0
                for j in range(len(lst)-1, i, -1):
                    lst[j] = x
                    x += 1

            num = 0
            x = len(lst)-1
            for j in range(len(lst)-1):
                num += lst[j]*(10**x)
                x -= 1
            num += lst[len(lst)-1]
            break

    if check == True:
        cnt += 1
        if cnt == n:
            print(num)
            sys.exit()
        num += 1

    if cnt >= 500000 or num > 9876543210: #가장 큰 감소하는 수가 9876543210 > 따라서 그 이상의 수에서는 exit
        print("-1")
        sys.exit()

# 두번째 풀이 : combination을 이용해 모든 감소하는 수를 포함하는 list를 만듦
import sys
r = sys.stdin.readline
from itertools import combinations

n = int(r())
lst = []

for i in range(1, 11):
    for j in combinations(range(10), i):
        j = list(j)
        j.sort(reverse=True)
        lst.append(int((''.join(str(x) for x in j))))

lst.sort()

try:    
    print(lst[n])
except:
    print("-1")
