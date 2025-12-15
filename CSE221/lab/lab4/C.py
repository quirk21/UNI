def matrix(node):
    arr = [[0]*node for _ in range(node)]
    for i in range(node):
        usr = list(map(int, input().split()))
        for j in range(usr[0]):
            arr[i][usr[j+1]] = 1
    for i in arr:
        print(*i)

res = matrix(int(input()))
