import sys
r = sys.stdin.readline

input = r().rstrip()
result = ""

for i in range(len(input)):
    if input[i] >= 'A' and input[i] <= 'Z':
        x = ord(input[i]) + 13
        if x > ord('Z'):
            x -= 26
        result += chr(x)
    elif input[i] >= 'a' and input[i] <= 'z':
        x = ord(input[i]) + 13
        if x > ord('z'):
            x -= 26
        result += chr(x)
    else:
        result += input[i]

print(result)