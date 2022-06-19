''''
<미로 찾기>
N x M 크기의 직사각형 형태의 미로에 여러 마리의 괴물이 있어 이를 피해 탈출해야 한다. 현재 위치는 (1, 1)이고 미로의 출구는 (N,M)의 위치에 존재하며 한 번에 한 칸씩 이동할 수 있다. 
괴물이 있는 부분은 0으로, 괴물이 없는 부분은 1로 표시되어 있다. 미로는 반드시 탈출할 수 있는 형태로 제시된다. 
탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하라. 칸을 셀 때는 시작 칸과 마지막 칸을 모두 포함해서 계산한다.

-input-
첫째 줄에 두 정수 N, M(4 <= N, M <= 200)이 주어진다. 다음 N개의 줄에는 각각 M개의 정수(0혹은 1)로 미로의 정보가 주어진다. 
각각의 수들은 공백 없이붙어서 입력으로 제시된다. 또한 시작 칸과 마지막 칸은 항상 1이다.
-output-
첫째 줄에 최소 이동 칸의 개수를 출력한다.

>> queue를 사용해서 해당 칸에 그 칸에 도달하기 위해 지나온 칸 수를 저장하는 방식으로 구현, 가장 마지막 칸에 들어있는 수를 출력한다.
''''

import sys
from collections import deque
r = sys.stdin.readline

n, m = map(int, r().split(" "))
lst = [list(map(int, r().rstrip())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0 , 1, -1]
queue = deque()
queue.append((0, 0))

def bfs(x, y):
    global lst

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx>=0 and ny>=0 and nx<n and ny<m:
                if lst[nx][ny] == 1:
                    queue.append((nx, ny))
                    lst[nx][ny] = lst[x][y] + 1

bfs(0, 0)
print(lst[n-1][m-1])
