class Node:
    def __init__(self, value, weight):
        self.val = value
        self.weight = weight
        self.next = None
 
def adj_list(node, edge):
    arr = [None]*node
    start = list(map(int, input().split()))
    end = list(map(int, input().split()))
    weight = list(map(int, input().split()))
 
    for i in range(edge):
        new = Node(end[i], weight[i])
        if arr[start[i]-1] != None:
            head = arr[start[i]-1]
            while head.next:
                head = head.next
            head.next = new
        else:
            arr[start[i]-1] = new
    return arr
 
usr = input().split()
res = adj_list(int(usr[0]), int(usr[1]))
for i in range(int(usr[0])):
    print(i+1,":",end=" ")
    head = res[i]
    if head == None:
        print()
        continue
    while head:
        print(f"({head.val},{head.weight})",end=" ")
        head = head.next
    print()
 