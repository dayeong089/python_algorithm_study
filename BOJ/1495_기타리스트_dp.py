# 처음 풀이 - 리스트 활용
import sys
r = sys.stdin.readline

n, s, m = map(int, r().split(" "))
lst = list(map(int, r().split(" ")))
result = [s]
now_lst = []

for i in range(n):
    for j in result:
        x1 = j+lst[i]
        x2 = j-lst[i]
        if 0<=x1<=m:
            now_lst.append(x1)
        if 0<=x2<=m:
            now_lst.append(x2)
    if len(now_lst) == 0:
        print("-1")
        sys.exit()
    result.clear()
    for i in now_lst:
        result.append(i)
    now_lst.clear()

print(max(result))
'''
리스트를 활용하였으나 메모리 초과가 뜸
그 이유를 찾아보니
30 500 1000
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
이와 같은 input을 넣으면 계속해서 중복이 일어나며 거의 2^30정도의 메모리가 필요
따라서 중복을 방지할 방법을 고민하다 set을 쓰기로 함
'''

# 최종 풀이 - set 활용
import sys
r = sys.stdin.readline

n, s, m = map(int, r().split(" "))
lst = list(map(int, r().split(" ")))
result = set([s])
now_lst = set([])

for i in range(n):
    for j in result:
        x1 = j+lst[i]
        x2 = j-lst[i]
        if 0<=x1<=m:
            now_lst.add(x1)
        if 0<=x2<=m:
            now_lst.add(x2)
    if len(now_lst) == 0:
        print("-1")
        sys.exit()
    result.clear()
    for i in now_lst:
        result.add(i)
    now_lst.clear()

print(max(result))
