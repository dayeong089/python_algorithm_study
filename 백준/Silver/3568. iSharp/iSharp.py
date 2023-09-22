import sys
r = sys.stdin.readline

sent = r().rstrip().split(" ")
lst1 = [[] for _ in range(len(sent))]
lst2 = [[] for _ in range(len(sent))]

for i in range(1, len(sent)):
    for j in sent[i]:
        if j==',' or j==';' or j=='[':
            pass
        elif j==']':
            lst1[i].append('[]')
        elif j=='&' or j=='*':
            lst1[i].append(j)
        else:
            lst2[i].append(j)

for i in range(1, len(lst1)):
    result = sent[0]
    for j in range(len(lst1[i])-1, -1, -1):
        result += lst1[i][j]
    result += " "
    for j in range(len(lst2[i])):
        result += lst2[i][j]
    result += ";"
    print(result)