import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())
edge_list = []
parent = [i for i in range(N+1)]
rank = [0]*(N+1)

for _ in range(M):
    u, v, w = map(int, input().split())
    edge_list.append((u, v, w))
edge_list.sort(key=lambda x:x[2])

def find(x, parent):
    if parent[x] != x:
        parent[x] = find(parent[x], parent)
    return parent[x]

def union(u, v, parent, rank):
    rootU = find(u, parent)
    rootV = find(v, parent)
    if rootU == rootV:
        return False
    if rank[rootV] > rank[rootU]:
        rootU, rootV = rootV, rootU
    if rank[rootU] == rank[rootV]:
        rank[rootU] += 1
    parent[rootV] = rootU
    return True 

# the first mst
first_weight = 0
first_path = []
for i in range(len(edge_list)):
    u, v, w = edge_list[i]
    if union(u, v, parent, rank):
        first_path.append(i)
        first_weight += w
if len(first_path) != N-1:
    print(-1)
    exit()

result = float('inf')

# exclude mst edge onebyone
for i in first_path:
    parent = [i for i in range(N+1)]
    rank = [0]*(N+1)
    count = 0
    weight = 0
    for j in range(len(edge_list)):
        if i == j:
            continue
        u, v, w = edge_list[j]
        if union(u, v, parent, rank):
            count += 1
            weight += w
    if count == N-1 and first_weight < weight:
        result = min(result, weight)

#include each non mst edge
non_mst_edges = [i for i in range(M) if i not in first_path]
for i in non_mst_edges:
    parent = [i for i in range(N+1)]
    rank = [0]*(N+1)
    count = 0
    weight = 0
    # Include non mst edge first
    u, v, w = edge_list[i]
    if union(u, v, parent, rank):
        count += 1
        weight += w
    # remaining edges
    for j in range(len(edge_list)):
        if i == j:
            continue
        u, v, w = edge_list[j]
        if union(u, v, parent, rank):
            count += 1
            weight += w
    if count == N-1 and first_weight < weight:
        result = min(result, weight)

print(result if result != float('inf') else -1)