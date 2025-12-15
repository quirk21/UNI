import sys
from collections import deque

N = int(sys.stdin.readline())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    start, end = map(int, sys.stdin.readline().split())
    graph[start].append(end)
    graph[end].append(start)

def Farthest_Node(start, graph, N):
    visited = [-1]*(N+1)
    q = deque([start])
    visited[start] += 1

    while q:
        node = q.popleft()
        for nx in graph[node]:
            if visited[nx] == -1:
                visited[nx] = visited[node] + 1
                q.append(nx)

    farthest_node = start
    distance = 0
    for i in range(1, N + 1):
        if visited[i] > distance:
            distance = visited[i]
            farthest_node = i
    
    return farthest_node, distance

node1, _ = Farthest_Node(1, graph, N)
node2, diameter = Farthest_Node(node1, graph, N)
print(diameter)
print(node1, node2)