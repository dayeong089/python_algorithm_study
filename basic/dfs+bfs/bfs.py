from collections import deque

def bfs(start, graph, visited):
    queue = deque([start])
    visited[start] = True
    print(start, end=' ')

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                print(i, end=' ')
                visited[i] = True

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

bfs(1, graph, visited)
print("\n")
