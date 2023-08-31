import sys
import itertools
r = sys.stdin.readline

n = int(r())
lst = []
p = []
min_value = sys.maxsize

for i in range(n):
    now = list(map(int, r().split(" ")))
    lst.append(now)
    p.append(i+1)

teams = list(itertools.combinations(p, int(n/2)))

for team in teams:
    other_team = []
    for i in p:
        if i not in team:
            other_team.append(i)

    score1 = 0
    score2 = 0
    combs1 = list(itertools.permutations(team, 2))
    combs2 = list(itertools.permutations(other_team,2))

    for comb in combs1:
        score1 += lst[comb[0]-1][comb[1]-1]
    for comb in combs2:
        score2 += lst[comb[0]-1][comb[1]-1]

    result = abs(score1-score2)
    if result < min_value:
        min_value = result
    
print(min_value)