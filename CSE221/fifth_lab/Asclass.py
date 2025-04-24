class node:
    def __init__(self, val):
        self.val = val
        self.color = 0
        

n, e = map(int,input().split())
node_list = [ node (i+1) for i in range(n+1)]
arr = [[] for _ in range(int(n))]

for i in range(e):
    start, end = map(int, input().split())
    arr[start-1].append(node_list[end-1])
    arr[end-1].append(node_list[start-1])

def bfs(arr, start):
    q = [start]
    start.color = 1
    
    while q:
        temp = q.pop(0)
        print(temp.val, end= " ")
        for i in arr[temp.val-1]: 
            if i.color == 0:
                q.append(i)
                i.color = 1
    
bfs(arr, node_list[0])