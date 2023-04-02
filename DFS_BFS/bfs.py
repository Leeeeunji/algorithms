# BFS: Breadth-First Search
from collections import deque


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    
    while queue: # queue에 원소가 있을 동안 
        n = queue.popleft()
        print(n, end=' ')
            
        for i in graph[n]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
         
graph = [
    [], # index: 0은 취급 X
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

bfs(graph, 1, visited)

