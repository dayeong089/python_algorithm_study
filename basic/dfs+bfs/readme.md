# DFS/BFS
## 그래프를 탐색하기 위한 대표적인 두 가지 알고리즘

### 스택(stack)
* FIRST IN LAST OUT
* append, pop 함수 사용

### 큐(queue)
* FIRST IN FIRST OUT
* collections 모듈에서 제공하는 deque 자료구조 사용
* append, popleft 함수 사용

## 재귀함수(recursion)
* 자기 자신을 다시 호출하는 함수
* 특정 조건일 때 재귀 함수를 더 이상 호출하지 않도록 종료조건을 꼭 명시해주어야함
* 재귀 함수의 수행은 스택 자료구조를 이용 (가장 마지막에 호출한 함수가 먼저 수행을 끝나야 다음 함수의 호출이 종료된다)
* 수학적 점화식(재귀식)을 그대로 코드로 옮긴 것이기 때문에 코드가 더 간결하다
