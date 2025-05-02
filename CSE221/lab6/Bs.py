from collections import defaultdict, deque
import sys

def bfs(graph, col, root):
    q = deque([root])
    col[root] = 0
    count = [1, 0]
    while q:
        root = q.popleft()
        for nx in graph[root]:
            if col[nx] == -1:
                col[nx] = col[root]^1 
                count[col[nx]] += 1        
                q.append(nx)

    return max(count)

def main():
    N, M = map(int, sys.stdin.readline().split())
    col = [-1]*(N+1)
    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    res= 0
    for i in range(1, N + 1):
        if col[i] == -1:
            res += bfs(graph, col, i)

    print(res)

main()