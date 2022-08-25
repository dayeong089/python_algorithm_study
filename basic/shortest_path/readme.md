# 최단 경로
## 가장 짧은 경로를 찾는 알고리즘

### 다익스트라 최단 경로 알고리즘
* 기본적으로 그리디 알고리즘으로 분류 > 매번 가장 비용이 적은 노드를 선택하여 임의의 과정을 반복
* 특정 노드에서 출발하여 다른 노드로 가는 각각의 최단 경로를 구해주는 알고리즘
* 음의 간선이 없을 때 정상적으로 동작
* 각 노드에 대한 현재까지의 최단 거리 정보를 1차원 리스트에 저장하며 리스트를 계속 갱신
* (1) 출발 노드 > 다른 모든 노드로의 최단 거리를 무한으로 초기화 : int(1e9)로 초기화
* (2) 방문하지 않은 노드 중 최단 거리가 가장 짧은 노드 선택
* (3) 그 노드를 거쳐서 갈 수 있는 노드까지의 거리를 확인하고 기존 리스트 값보다 작으면 값을 갱신 