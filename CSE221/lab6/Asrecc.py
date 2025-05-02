import sys
sys.setrecursionlimit(2*100000+50)

nodes, edges = map(int, input().split())
graph = [[] for _ in range(nodes+1)]

for i in range(edges):
    start, end = map(int, input().split())
    graph[start].append(end)

visited = [-1]*(nodes+1)
stack = []

def topo_sort(graph, visited, root, stack):
    
        visited[root] += 1
        for nx in graph[root]:
            if visited[nx] == -1:
                if topo_sort(graph, visited, nx, stack): return True
            elif visited[nx] == 0: return True
        visited[root] += 1
        stack.append(root)
        return False

def main():
    for i in range(1, nodes+1):
        if visited[i] == -1: 
            if topo_sort(graph, visited, i, stack): return True
    return False

bool = main()

if not bool: 
    for i in range(nodes-1,-1,-1): print(stack[i], end=" ")
else:
    print(-1)