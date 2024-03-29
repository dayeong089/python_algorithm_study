# 다이나믹 프로그래밍
## 개념
* 메모리 공간을 더 사용하면서 연산 속도를 비약적으로 증가
* 조건 > 큰 문제를 작은 문제로 나눌 수 있어야 하며, 작은 문제에서 구한 정답이 그것을 포함하는 큰 문제에서도 동일해야 함
* 큰 문제를 작게 나누고, 같은 문제라면 한 번씩만 풀어서 문제를 효율적으로 해결

## 메모리제이션(캐싱)
* 한번 구한 결과를 메모리 공간에 메모해두고 같은 식을 다시 호출하면 메모한 결과를 그대로 가져오는 기법
* 한번 구한 정보를 리스트에 저장해두고 같은 정보가 필요할 때 리스트에서 해당 값을 가져온다

## 탑다운 방식 & 보텀업 방식
* 탑다운 방식 : 큰 문제를 해결하기 위해 작은 문제를 호출 > 재귀 함수를 이용한 dp
* 보텀업 방식 : 작은 문제부터 차근차근 답을 도출 > 반복문을 이용한 dp
* 메모리제이션은 탑다운 방식에 국한되어 사용되는 표현
* 재귀 함수의 스택 크기가 한정되어 recursion depth 관련 오류가 발생할 수 있으므로 보텀업 방식을 선호
* sys.setrecursionlimit()을 이용하여 재귀 제한을 완화할 수 
