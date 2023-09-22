import sys
r = lambda:sys.stdin.readline().rstrip()

sent = r().split(" ")
for i in range(1, len(sent)):
    idx = 0
    sent[i] = sent[i].replace(";",",")
    for j in range(len(sent[i])):
        if sent[i][j] in ["*", "&", "[", ","]:
            idx = j
            break
    print(sent[0]+sent[i][j:][::-1].replace("][", "[]").replace(",", ""), sent[i][:j]+";")
