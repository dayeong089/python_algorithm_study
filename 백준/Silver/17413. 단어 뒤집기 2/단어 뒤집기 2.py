import sys
r = sys.stdin.readline

input = r().rstrip()
result = ""
part = ""
mode = False

for i in range(len(input)):
	if input[i] == '<':
		result += part[::-1]
		result += input[i]
		part = ""
		mode = True
	elif input[i] == '>':
		result += input[i]
		mode = False
	elif mode == True:
		result += input[i]
	elif input[i] == ' ':
		result += part[::-1]
		result += input[i]
		part = ""
	else:
		part += input[i]
		
result += part[::-1]
	
print(result)