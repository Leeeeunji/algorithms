# 연습 문제: 미로 탈출
from collections import deque
n, m = map(int, input().split())

maze = [[]*m for _ in range(n)]
for i in range(n):
    maze[i] = list(map(int, input()))

def bfs(maze, first_x, first_y):
    queue = deque([(first_x, first_y)])
    count = 0
    while queue:
        x, y = queue.popleft()
        
        if x < 0 or x >= n or y < 0 or y >= m:
            continue
        if maze[x][y] == 1: # 아직 방문 X 길일때
            maze[x][y] = 0 # 방문 했다고 표시
            count += 1 # 방문한 길 + 1
            if x == n-1 and y == m-1: # 목적지 도착
                print(count)
                return
            queue.append((x+1, y))
            queue.append((x, y+1))
            
# count = 0          
# bfs(count, maze, 0, 0)
# print(count) # 이렇게 하면 당연히 안됨! C 포인터도 아니고,,
bfs(maze, 0, 0)