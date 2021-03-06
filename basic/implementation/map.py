''''
<상하좌우>
여행가 A는 N × N 크기의 정사각형 공간 위에 서 있다. 이 공간은 1 × 1 크기의 정사각형으로 나누어져 있다.
가장 왼쪽 위 좌표는 (1, 1)이며, 가장 오른쪽 아래 좌표는 (N, N)에 해당한다.
여행가 A는 상, 하, 좌, 우 방향으로 이동할 수 있으며, 시작 좌표는 항상 (1, 1)이다. 우리 앞에는 여행가 A가 이동할 계획이 적힌 계획서가 놓여 있다

계획서에는 하나의 줄에 띄어쓰기를 기준으로 L, R, U, D 중 하나의 문자가 반복적으로 적혀있다.

L: 왼쪽으로 한 칸 이동
R: 오른쪽으로 한 칸 이동
U: 위로 한 칸 이동
D: 아래로 한 칸 이동

이때 여행가 A가 N × N 크기의 정사각형 공간을 벗어나는 움직임은 무시된다

-input-
첫째 줄에 공간의 크기를 나타내는 N이 주어집니다. (1<=N<=100)
둘째 줄에 여행가 A가 이동할 계획서 내용이 주어집니다. (1<=이동 횟수<=100)
-output-
첫째 줄에 게임의 룰에 맞게 선택한 카드에 적힌 숫자를 출력

>> 시뮬레이션 : 일련의 명령에 따라서 개체를 차례대로 이동
>> L, R, U, D 각 경우에 따라 예외상황(정사각형 공간을 벗어나는 경우)을 고려하며 처리해준다.
>> + 추가 구현 : 배열을 더 잘 활용

''''
# 구현 1
import sys
r = sys.stdin.readline

n = int(r())
lst = list(r().rstrip().split(" "))
x1 = 1
y1 = 1

print(lst)

for x in lst:
    if x == "L" and y1 > 1:
        y1 -= 1
    elif x == "R" and y1 < 5:
        y1 += 1
    elif x == "U" and x1 > 1:
        x1 -= 1
    elif x == "D" and x1 < 5:
        x1 += 1

print(x1, y1)

# 구현 2
import sys
r = sys.stdin.readline

n = int(r())
lst = list(r().rstrip().split(" "))
x, y = 1, 1

move = ["L", "R", "U", "D"]
mx = [0, 0, -1, 1]
my = [-1, 1, 0, 0]

for now in lst:
    for i in range(len(move)):
        if now == move[i]:
            tmpx = x + mx[i]
            tmpy = y + my[i]

    if tmpx > 0 and tmpx <=n and tmpy > 0 and tmpy <= n:
        x = tmpx
        y = tmpy

print(x, y)
