import sys
sys.setrecursionlimit(2*100000+50)

data = list(map(int, sys.stdin.read().split()))
start = data[2:int(data[1])+2:1]
end = data[int(data[1])+2::]

graph = [[] for _ in range(data[0]+1)]
visited = set()
for i in range(1,data[1]+1):
    graph[start[i-1]].append(end[i-1])
    graph[end[i-1]].append(start[i-1]) 

def dfs(graph, visited, root):
    if root not in visited:
        print(root, end=" ")
        visited.add(root)
        for i in graph[root]:
            dfs(graph, visited, i)

dfs(graph, visited, 1)
