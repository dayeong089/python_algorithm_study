N = int(input())
array = [0]*865

for i in range(123, 988):
    x1 = i//100
    x2 = (i%100)//10
    x3 = (i%100)%10
    if x1==x2 or x2==x3 or x3==x1:
        array[i-123] = 1
    if x2==0 or x3==0:
        array[i-123] = 1
        
for i in range(N):
    num, s, b = map(int, input().split(" "))
    y1 = num//100
    y2 = (num%100)//10
    y3 = (num%100)%10
    list1 = [y1, y2, y3]
    
    for j in range(123, 988):
        if array[j-123] == 0:
            s1 = 0
            b1 = 0
            x1 = j//100
            x2 = (j%100)//10
            x3 = (j%100)%10
            if x1 == y1:
                s1 += 1
            elif x1 == y2 or x1 == y3:
                b1 += 1
            
            if x2 == y2:
                s1 += 1
            elif x2 == y1 or x2 == y3:
                b1 += 1

            if x3 == y3:
                s1 += 1
            elif x3 == y1 or x3 == y2:
                b1 += 1

            if s1 != s or b1 != b:
                array[j-123] = 1

cnt = 0
for i in range(123, 988):
    if array[i-123] == 0:
        cnt += 1

print(cnt)