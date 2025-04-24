import sys
sys.setrecursionlimit(2*100000+50)
n, e = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]

for _ in range(e):
    start, end = map(int, sys.stdin.readline().split())
    graph[start].append(end)

def dfs(graph, node, visited):
    visited[node] += 1 # directly assignning will also work
    for nx in graph[node]:
        if visited[nx] == -1:
            if dfs(graph, nx, visited): return True 
        elif visited[nx] == 0: return True
    visited[node] += 1     
    return False

# -1 not visited
# 0 in stack
# 1 done visiting
def has_cycle(graph, n):
    visited = [-1] * (n + 1)

    for node in range(1, n + 1):
        if visited[node] == -1:
            
            if dfs(graph, node, visited):
                return True
    return False


if has_cycle(graph, n):
    print("YES")
else:
    print("NO")