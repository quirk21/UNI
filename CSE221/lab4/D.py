def eularian_path(node, edge) :
    arr = [0]*node
    
    start = list(map(int, input().split()))
    end = list(map(int, input().split()))
    
    for i in range(edge):
        arr[start[i]-1] += 1
        arr[end[i]-1] += 1
    
    count = 0
    for i in arr:
        if i % 2 != 0:
            count += 1
        if count > 2:
            return "NO"
    if count == 0 or count == 2:
        return "YES"
    return "NO"
    
usr = input().split()
print(eularian_path(int(usr[0]), int(usr[1])))