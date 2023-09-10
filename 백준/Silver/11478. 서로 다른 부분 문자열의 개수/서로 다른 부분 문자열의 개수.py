import sys
r = lambda: sys.stdin.readline().rstrip()

s = r()
lst = []
for i in range(len(s)+1):
    for j in range(i+1, len(s)+1):
        lst.append(s[i:j])

print(len(set(lst)))