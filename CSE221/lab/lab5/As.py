node, edge = input().split()
arr = [[] for _ in range(int(node))]
for i in range(int(edge)):
    start, end = map(int, input().split())
    arr[start-1].append(end)
    arr[end-1].append(start)
 
def bfs(arr, node):
    visited = [False] * (node+1)
    visited[1] = True
    queue = [1] 
    while queue:
        node = queue.pop(0)
        print(node, end= " ")
        for i in arr[node-1]: 
            if not visited[i] and i != 0:
                visited[i] = True
                queue.append(i)
   
bfs(arr, int(node))