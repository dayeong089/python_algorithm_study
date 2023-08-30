import sys
r = sys.stdin.readline

e, s, m = map(int, r().split(" "))

for i in range(1, 7981):
    if (i%15 == 0 and e == 15) or (i%15 == e):
        if(i%28 == 0 and s == 28) or (i%28 == s):
            if(i%19 == 0 and m == 19) or (i%19 == m):
                print(i)
                break
