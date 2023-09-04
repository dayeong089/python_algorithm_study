import sys
r = sys.stdin.readline

table = {"A+":4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0}

total_score = 0.0
total_num = 0.0
for i in range(20):
    subject, num, score = r().rstrip().split(" ")
    if score == 'P': continue
    total_score += (table[score] * float(num))
    total_num += float(num)

print(total_score/total_num)