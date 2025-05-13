import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

N,M = map(int, input().split())
edges = []
par = [i for i in range(N+1)]

for _ in range(M):
    u, v, w = map(int, input().split())
    edges.append((w, u, v))

def find(x):
    if par[x] != x:
        par[x] = find(par[x])
    return par[x]

edges.sort() # sort the edges in non-decreasing order
path_cost = 0 
for w, u, v in edges:
    root_u = find(u)
    root_v = find(v)
    if root_u != root_v:
        par[root_v] = root_u
        path_cost += w

print(path_cost)