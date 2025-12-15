def eularian_path(node, edge) :
    arr = [0]*node
    
    start = list(map(int, input().split()))
    end = list(map(int, input().split()))
    
    for i in range(edge):
        arr[start[i]-1] -= 1
        arr[end[i]-1] += 1
    
    print(*arr)
    
    
usr = input().split()
eularian_path(int(usr[0]), int(usr[1]))