import sys, heapq

# taking input and building graph
N,M,S,D = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
start = list(map(int, sys.stdin.readline().split()))
end = list(map(int, sys.stdin.readline().split()))
weight = list(map(int, sys.stdin.readline().split()))

for i in range(M):
    graph[start[i]].append(( weight[i],end[i]))

def dijkstra(graph: list[list[int]], source: int, destination: int , node: int) -> tuple[list[int], list[int]]:
    distance = [float('inf')]*(node+1)
    prev = [-1]*(node+1)
    minheap = []
    distance[source] = 0
    heapq.heappush(minheap,(0, source))

    while minheap:
        curr_dis, curr_node = heapq.heappop(minheap)
        # if we aleready have a shorter path iteration is skipped
        if curr_dis > distance[curr_node]: continue

        for nx_dis, nx_node in graph[curr_node]:
            temp = curr_dis + nx_dis
            if temp < distance[nx_node]:
                distance[nx_node] = temp
                prev[nx_node] = curr_node
                heapq.heappush(minheap, (temp, nx_node))
    
    return distance, prev

distance, prev = dijkstra(graph, S, D, N)

if distance[D] == float('inf'):
    print(-1)
else:
    # creating path
    cur = D 
    path = []
    while cur != -1:
        path.append(cur)
        cur = prev[cur]
    path.reverse()
    print(distance[D])
    print(' '.join(map(str, path)))
