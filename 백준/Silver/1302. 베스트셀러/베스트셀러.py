import sys
r = sys.stdin.readline

n = int(r())
book = {}

for i in range(n):
    title = r().rstrip()
    if title in book:
        book[title] += 1
    else:
        book[title] = 1

max_num = 0
max_title = ""

for title in book.keys():
    if book[title] > max_num:
        max_num = book[title]
        max_title = title
    elif book[title] == max_num:
        lst = []
        lst.append(title)
        lst.append(max_title)
        lst.sort()
        max_title = lst[0]

print(max_title)