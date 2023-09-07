num = int(input())
cnt = 0
for i in range(num):
    now = input()
    list = []
    check = True
    for j in range(len(now)):
        if list.count(now[j]) == 0:
            list.append(now[j])
        else:
            if j>0 and now[j-1] == now[j]:
                pass
            else:
                check = False
    if check == True:
        cnt += 1

print(cnt)