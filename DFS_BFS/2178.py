# [실버1] 미로 탐색
from collections import deque
n, m = map(int, input().split())
maze = []
for _ in range(n):
    maze.append(list(map(int, input())))

def bfs(maze, x, y):
    queue = deque([(x, y)]) 
    count = 0
    while queue:
        x, y = queue.popleft()
        if x < 0 or y < 0 or x >= n or y >= m:
            continue
        if maze[x][y] == 1:
            maze[x][y] = 0
            count += 1
            if x==n-1 and y==m-1:
                print(count)
                return
            queue.append((x+1, y))
            queue.append((x-1, y))
            queue.append((x, y+1))
            queue.append((x, y-1))
            
bfs(maze, 0, 0)