from collections import deque

N,M,S,D,K = map(int, input().split())
graph = [[] for _ in range(N+1)]
for i in range(M):
    start, end = map(int, input().split())
    graph[start].append(end) 

for i in graph:
    i.sort()

def bfs_shortest_path( graph,n, s, t):
    parent = [-1] * (n + 1)
    dist = [-1] * (n + 1)
    
    queue = deque()
    queue.append(s)
    dist[s] = 0

    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if dist[i] == -1:
                parent[i] = node
                dist[i] = dist[node] + 1
                queue.append(i)

    if dist[t] == -1:
        return


    path = []
    curr = t
    while curr != -1:
        path.append(curr)
        curr = parent[curr]
    path.reverse()

    return path

path1 = bfs_shortest_path(graph, N, S, K)
path2 = bfs_shortest_path(graph, N, K, D)

if not path1 or not path2:
    print(-1)
else:
    result = path1+path2[1:]
    print(len(result)-1)
    print(*result)