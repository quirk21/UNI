import sys, heapq

# taking input and building graph
N,M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
start = list(map(int, sys.stdin.readline().split()))
end = list(map(int, sys.stdin.readline().split()))
weight = list(map(int, sys.stdin.readline().split()))
for i in range(M):
    graph[start[i]].append(( weight[i],end[i]))

def dijkstra(graph: list[list[int]], source: int, destination: int , node: int) -> int:
    distance = [[float('inf')] * 2 for _ in range(node + 1)] # every node will store two distance. for odd/even
    distance[source][0] = 0 # initializing both of those distance as 0
    distance[source][1] = 0 
    minheap = [(distance[source][0], source, 0), (distance[source][1], source, 1)] # this minheap will carry both even/odd option for first node 
    heapq.heapify(minheap)   # as every other node has more distance than first node, this first two initialization will run with all of the neighbors of first node
                             # then we will start with the closest neighbor and rest of the code will have one parity in minheap
    while minheap:
        curr_dis, curr_node, curr_parity = heapq.heappop(minheap)
        # if we aleready have a shorter path iteration is skipped
        if curr_dis > distance[curr_node][curr_parity]: continue
        
        for nx_dis, nx_node in graph[curr_node]:
            nx_parity = nx_dis % 2        
            if curr_parity != nx_parity: # checking the parity of weight/distance
                temp = curr_dis + nx_dis
                if temp < distance[nx_node][nx_parity]:
                    distance[nx_node][nx_parity] = temp
                    heapq.heappush(minheap, (temp, nx_node, nx_parity))  # passing the neighbors' parity in minheap
        # end of dijkstra

    min_dist = min(distance[destination][0], distance[destination][1]) # we will have two values for one node
    return min_dist if min_dist != float('inf') else -1                

print( dijkstra(graph, 1, N, N))

