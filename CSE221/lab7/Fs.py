import sys, heapq

# taking input
N, M, S, D = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]

for i in range(M):
    start, end, weight = map(int, sys.stdin.readline().split())
    graph[start].append((weight, end))
    graph[end].append((weight, start))  # Add reverse edge for undirected graph

def second_shortest_path(graph: list[list[int]], source: int, destination: int, node:int) -> int:
    # dist[node][0]: shortest distance, dist[node][1]: second shortest distance
    dist = [[float('inf')]*2 for _ in range(node + 1)]
    dist[source][0] = 0
    minheap = [] 
    heapq.heappush(minheap,(0, source))

    while minheap:
        curr_dist, curr_node = heapq.heappop(minheap)
        # if we aleready have a shorter path iteration is skipped
        if curr_dist > dist[curr_node][1]: continue

        for nx_dist, nx_node in graph[curr_node]:
            new_dist = curr_dist + nx_dist

            # Update shortest distance
            if new_dist < dist[nx_node][0]:
                # Current shortest becomes second shortest
                dist[nx_node][1] = dist[nx_node][0]
                dist[nx_node][0] = new_dist
                heapq.heappush(minheap, (new_dist, nx_node))

            # Update second shortest distance if strictly greater than shortest
            elif new_dist > dist[nx_node][0] and new_dist < dist[nx_node][1]:
                dist[nx_node][1] = new_dist
                heapq.heappush(minheap, (new_dist, nx_node))

    return dist[destination][1] if dist[destination][1] != float('inf') else -1

print(second_shortest_path(graph, S, D, N))