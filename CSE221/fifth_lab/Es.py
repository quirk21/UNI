import sys
sys.setrecursionlimit(2*100000+50)
n, e = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]

for _ in range(e):
    start, end = map(int, sys.stdin.readline().split())
    graph[start].append(end)

def dfs(graph, node, visited, back):
    visited[node] = True
    back[node] = True

    for i in graph[node]:
        if not visited[i]:
            if dfs(graph, i, visited, back):
                return True
        elif back[i]:
            return True 

    back[node] = False
    return False

def has_cycle(graph, n):
    visited = [False] * (n + 1)
    back = [False] * (n + 1)

    for node in range(1, n + 1):
        if not visited[node]:
            if dfs(graph, node, visited, back):
                return True
    return False


if has_cycle(graph, n):
    print("YES")
else:
    print("NO")