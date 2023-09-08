import sys
r = sys.stdin.readline

strings = []
s = r().rstrip()
for i in range(len(s)):
    strings.append(s[i:])

strings.sort()

for string in strings:
    print(string)