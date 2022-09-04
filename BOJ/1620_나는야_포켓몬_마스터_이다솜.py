# dict
# code1
import sys
r = sys.stdin.readline

n, m = map(int, r().split(" "))
data = dict()
result = []

for i in range(1, n+1):
    x = r().rstrip()
    data[str(i)]=x

key_list = data.keys()
data2 = {v:k for k,v in data.items()}
key_list2 = data2.keys()

for _ in range(m):
    x = r().rstrip()
    if x in key_list:
        result.append(data[x])
    elif x in key_list2:
        result.append(data2[x])

for i in result:
    print(i)

# code2
import sys
r = sys.stdin.readline

n, m = map(int, r().split(" "))
data = dict()

for i in range(1, n+1):
    x = r().rstrip()
    data[i]=x
    data[x]=i

for _ in range(m):
    x = r().rstrip()
    if x.isdigit():
        print(data[int(x)])
    else:
        print(data[x])
