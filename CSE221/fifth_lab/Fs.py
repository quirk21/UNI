from collections import deque
R, H = map(int, input().split())
graph = [list(input()) for _ in range(R)]
direction = [(0, -1), (0, 1), (1, 0), (-1, 0)]

def bfs(i, j):
    q = deque()
    q.append((i,j))
    temp = 1 if graph[i][j] == "D" else 0
    graph[i][j] = '#'

    while q:
        x, y = q.popleft()
        for dx, dy in direction:
            nx, ny = x+dx, y+dy
            if 0<= nx< R and 0<= ny< H and graph[nx][ny] in ['.','D']:
                if graph[nx][ny] == 'D':
                    temp += 1
                graph[nx][ny] = '#'
                q.append((nx, ny))
    return temp

def collect_diamond():
    count = 0
    for i in range(R):
        for j in range(H):
            if graph[i][j] in ['.', 'D']:
                count = max(count,  bfs(i, j))
    return count

print(collect_diamond())