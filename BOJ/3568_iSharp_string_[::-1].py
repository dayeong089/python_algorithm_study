# 내풀이
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
    
# [::-1] - 문자열 거꾸로 출력, replace를 활용해서 더 간단하게 풀수도 있음
import sys
r = sys.stdin.readline

sent = r().rstrip().split(" ")
for i in range(1, len(sent)):
    idx = 0
    sent[i] = sent[i].replace(";",",")
    for j in range(len(sent[i])):
        if sent[i][j] in ["*", "&", "[", ","]:
            idx = j
            break
    print(sent[0]+sent[i][j:][::-1].replace("][", "[]").replace(",", ""), sent[i][:j]+";")
