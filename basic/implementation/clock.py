''''
<시각>
정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성하라. 

-input-
첫째 줄에 정수 N이 입력된다.(0<=N<=23)
-output-
00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 출력한다.

>> 완전 탐색 : 모든 경우의 수를 고려
>> 시, 분, 초를 합쳐서 하나의 문자열로 만든 다음, 3이 문자열에 포함되어 있는지 확인한다.

''''
import sys
r = sys.stdin.readline

n = int(r())
cnt = 0

for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if "3" in str(i)+str(j)+str(k):
                cnt += 1

print(cnt)
