def king_of_kon(N, x, y):
    arr = []
    directions = [(-1, -1), (-1, 0), (-1, +1), ( 0, -1), ( 0, +1), (+1, -1), (+1, 0), (+1, +1)]
    
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 1 <= nx <= N and 1 <= ny <= N:
            arr.append((nx, ny))
    
    arr.sort()
    print(len(arr))
    for i in arr:
        print(i[0]," ",i[1])

N = int(input())
x, y = input().split()
king_of_kon(N,int(x),int(y))