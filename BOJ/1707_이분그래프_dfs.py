import sys
r = sys.stdin.readline

# 연결된 정점끼리 다른 list에 저장(y값을 통해 분별)
def dfs(x, y):
    stack = []
    stack.append((x, y))
    visited[x] = True

    while stack:
        x, y = stack.pop()
        if y%2 == 0:
            lst1.append(x)
        else:
            lst2.append(x)
            
        for i in graph[x]:
            if visited[i] == False:
                stack.append((i, y+1))
                visited[i] = True
    return y

k = int(r())
for _ in range(k):
    v, e = map(int, r().split(" "))
    graph = [[] for _ in range(v+1)]
    visited = [False]*(v+1)
    lst1 = []
    lst2 = []
    
    # 그래프 입력
    for _ in range(e):
        x, y = map(int, r().split(" "))
        graph[x].append(y)
        graph[y].append(x)
        
    # 그래프가 연결되어 있지 않을 수 있으므로 dfs 이후에도 방문하지 않은 정점에 대해 다시 dfs
    cnt = 0
    for i in range(1, v+1):
        if visited[i] == False:
            cnt = dfs(i, cnt)
            
    # list를 in연산 했을때 시간 초과 발생 > set으로 변환
    lst1 = set(lst1)
    lst2 = set(lst2)
    
    # 같은 list에 있는 정점끼리 연결되어 있으면 False
    check = True
    for i in lst1:
        for j in graph[i]:
            if j in lst1:
                check = False

    for i in lst2:
        for j in graph[i]:
            if j in lst2:
                check = False

    if check == True:
        print("YES")
    else:
        print("NO")
