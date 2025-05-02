import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, R = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [0]*(N+1)

for _ in range(N-1):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

def dfs(node):
    visited[node] = 1
    size = 1 
    for nx in graph[node]:
        if visited[nx] == 0:
            size += dfs(nx) 
    visited[node] = size
    return size

dfs(R)

Q = int(input())
for _ in range(Q):
    query = int(input())
    print(visited[query])