import sys, heapq

# taking input and building graph
N,M,S,D = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
for i in range(M):
    start, end, weight = map(int, sys.stdin.readline().split())
    graph[start].append(( weight,end))

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
        # end of dijkstra

    return distance 

alice_distance = dijkstra(graph, S, D, N)
bob_distance = dijkstra(graph, D, S, N)

# finding the meeting point
min_time = float('inf') 
meet_node = -1
for i in range(1, N+1):
    a, b = alice_distance[i], bob_distance[i]
    if a == float('inf') or b == float('inf'):
        continue
    t = max(a, b) # maximum time to reach for one of them
    if t < min_time or (t == min_time and i < meet_node): # as this condition will run at least once so meet_node gets changed
        min_time = t
        meet_node = i

if meet_node == -1:
    print(-1)
else:
    print(min_time, meet_node)