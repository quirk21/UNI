from collections import deque

data = list(map(int, input().split()))
start = list(map(int, input().split()))
end = list(map(int, input().split()))

graph = [[] for _ in range(data[0])]

for i in range(data[1]):
    graph[start[i]-1].append(end[i]) 
    graph[end[i]-1].append(start[i])

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
        for i in graph[node-1]:
            if dist[i] == -1:
                parent[i] = node
                dist[i] = dist[node] + 1
                queue.append(i)

    if dist[t] == -1:
        print(-1)
        return


    path = []
    curr = t
    while curr != -1:
        path.append(curr)
        curr = parent[curr]
    path.reverse()

    print(dist[t])
    print(*path)

bfs_shortest_path( graph, data[0], data[2], data[3])