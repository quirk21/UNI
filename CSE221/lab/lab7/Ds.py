import sys, heapq

# taking inputs
N,M,S,D = map(int, sys.stdin.readline().split())
node_weight = list(map(int, sys.stdin.readline().split())) 
graph = [[] for _ in range(N+1)]
for i in range(M):
    start, end = map(int, sys.stdin.readline().split())
    graph[start].append(end)

def dijkstra(graph: list[list[int]], source: int, destination: int , node: int, node_weight: list) -> int:
    distance = [float('inf')]*(node+1)
    prev = [-1]*(node+1)
    minheap = []
    distance[source] = node_weight[source-1]
    heapq.heappush(minheap,(node_weight[source-1], source))

    while minheap:
        curr_dis, curr_node = heapq.heappop(minheap)
        # if we aleready have a shorter path iteration is skipped
        if curr_dis > distance[curr_node]: continue

        for nx_node in graph[curr_node]:
            nx_dis = node_weight[nx_node-1]
            temp = curr_dis + nx_dis
            if temp < distance[nx_node]:
                distance[nx_node] = temp
                prev[nx_node] = curr_node
                heapq.heappush(minheap, (temp, nx_node))
        # end of dijkstra

    if distance[destination] == float('inf'):
        return -1
    
    return distance[destination]


print(dijkstra(graph, S, D, N, node_weight))