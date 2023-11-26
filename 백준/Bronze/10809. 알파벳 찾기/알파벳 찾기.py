S = input()
num = 97

for i in range(26):
    print(S.find(chr(num+i)), end=" ")