import sys
r = sys.stdin.readline

n, k = map(int, r().split(" "))
lst1 = list(map(int, r().split(" ")))
lst2 = list(map(int, r().split(" ")))

lst1.sort()
lst2.sort(reverse = True)

for i in range(k):
    if lst2[i] > lst1[i]:
        lst1[i] = lst2[i]
    else:
        break

print(sum(lst1))
