A, B = map(int, input().split(" "))
C = int(input())
a = 0
b = B+C
c = A
if b>=60:
    a = b//60
    b = b%60
    c = A+a
    if c>=24:
        c-=24
print(c, b)
