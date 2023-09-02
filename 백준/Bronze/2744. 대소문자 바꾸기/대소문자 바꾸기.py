import sys
r = sys.stdin.readline

input = r().rstrip()
result = ""

for i in range(len(input)):
    if input[i] >= 'A' and input[i] <= 'Z':
        result += chr(ord(input[i]) - ord('A') + ord('a'))
    elif input[i] >= 'a' and input[i] <= 'z':
        result += chr(ord(input[i]) - ord('a') + ord('A'))
    else:
        result += input[i]
        
print(result)