sent = input()
sent = sent.upper()
cnt = []
for i in range(65, 91):
    cnt.append(sent.count(chr(i)))

max_value = max(cnt)
idx = cnt.index(max_value)
cnt.pop(idx)
if max_value in cnt:
    print("?")
else:
    print(chr(65+idx))