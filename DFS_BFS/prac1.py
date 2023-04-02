# 음료수 얼려 먹기
n, m = map(int, input().split())
visited = [[] * m for _ in range(n)]
for i in range(n):
    visited[i] = list(map(int, input()))
count = 0

def dfs(visited, x, y):
    if  x < 0 or x >= n or y < 0 or y >= m:
        return False
    if visited[x][y] == 0:
        visited[x][y] = 1
        dfs(visited, x+1, y)
        dfs(visited, x, y+1)
        return True
    else:
        return False
        
        
        ## count를 떼내어서 한 stack 계산이 마무리 될때만 count += 1이 되도록 해야함!
for i in range(n):
    for j in range(m):
        if dfs(visited, i, j):
            count += 1

print(count)