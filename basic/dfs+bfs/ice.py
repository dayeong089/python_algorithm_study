''''
<음료수 얼려먹기>
N × M 크기의 얼음 틀이 있다. 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시된다.
구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주한다.
이때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하라.

-input-
첫 번째 줄에 얼음 틀의 세로 길이 N과 가로 길이 M이 주어진다. (1 <= N, M <= 1,000)
두 번째 줄부터 N + 1 번째 줄까지 얼음 틀의 형태가 주어진다.
이때 구멍이 뚫려있는 부분은 0, 그렇지 않은 부분은 1이다.
-output-
한 번에 만들 수 있는 아이스크림의 개수를 출력한다.

>> DFS를 이용하여 한번 탐색하면서 해당 0과 이어져있는 모든 0을 1로 만들고 다시 탐색을 진행한다. 탐색한 횟수를 구하면 아이스크림 개수를 구할 수 있다.

import sys
r = sys.stdin.readline

N, M = map(int, r().split(" "))
graph = [list(map(int, r().rstrip())) for _ in range(N)]

def dfs(x, y):
    if x < 0 or x >= N or y < 0 or y >= M:
        return
    else:
        if graph[x][y] == 0:
            graph[x][y] = 1
            dfs(x-1, y)
            dfs(x+1, y)
            dfs(x, y-1)
            dfs(x, y+1)
            return

cnt = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            cnt += 1
            dfs(i, j)

print(cnt)
