def adj_mat(node, edge):
    arr = [[0]*node for _ in range(node)]
    for i in range(edge):
        num = list(map(int, input().split()))
        arr[num[0]-1][num[1]-1] = num[2]
    return arr
 
usr = list(map(int, input().split()))
res = adj_mat(usr[0], usr[1])
print('\n'.join(' '.join(map(str, row)) for row in res))