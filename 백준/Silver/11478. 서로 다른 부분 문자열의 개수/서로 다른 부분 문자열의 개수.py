import sys
r = sys.stdin.readline

s = r().rstrip()
lst = []
for i in range(len(s)+1):
    for j in range(i+1, len(s)+1):
        lst.append(s[i:j])

print(len(set(lst)))