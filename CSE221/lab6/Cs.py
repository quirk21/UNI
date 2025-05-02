from collections import deque
n = int(input()) 
startX, startY, endX, endY = map(int, input().split())

direction = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(-1,2),(1,-2),(-1,-2)]
graph = [[0]*(n+1) for _ in range(n+1)]

q = deque([(startX, startY, 0)])
flag = -1
while q:
    x, y, count = q.popleft()
    if (x, y) == (endX, endY):
        flag = count
        break 
    for dx, dy in direction: 
        nx, ny = x+dx, y+dy
        if 1 <= nx <= n and 1 <= ny <= n : 
            if graph[nx][ny] == 0: 
                graph[nx][ny] = 1          
                q.append((nx, ny, count + 1))

print(flag)