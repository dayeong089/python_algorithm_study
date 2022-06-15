def dfs(start, graph, visited):
    visited[start] = True
    print(start, end=' ')

    for i in graph[start]:
        if not visited[i]:
            dfs(i, graph, visited)


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

dfs(1, graph, visited)
print("\n")
