import sys, heapq

# taking input and building graph
N,M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
for i in range(M):
    start, end, weight = map(int, sys.stdin.readline().split())
    graph[start].append(( weight,end))
    graph[end].append(( weight,start))

def dijkstra(graph: list[list[int]], source: int, node: int) -> list[int]:
    # no need for prev/parent array in this problem as we just need the distance
    distance = [float('inf')]*(node+1)
    minheap = []
    distance[source] = 0
    heapq.heappush(minheap,(0, source))

    while minheap:
        curr_dis, curr_node = heapq.heappop(minheap)
        # if we aleready have a shorter path iteration is skipped
        if curr_dis > distance[curr_node]: continue

        for nx_dis, nx_node in graph[curr_node]:
            temp = max(curr_dis, nx_dis) # only taking the maximum danger lvl/distance
            if temp < distance[nx_node]: # we take the max of current and next edge and compare it with it's distance
                distance[nx_node] = temp
                heapq.heappush(minheap, (temp, nx_node))
        # end of dijkstra

    return distance 

lvl = dijkstra(graph, 1, N)

for i in range(1,N+1):
    if lvl[i] == float('inf'):
        print(-1, end=" ")
    else:
        print(lvl[i],end=" ")