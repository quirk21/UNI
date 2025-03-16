def csort(arr):
    minn = min(arr)
    maxx = max(arr)
    count = [0]*(maxx-minn+1)
    for i in arr:
        count[i-minn] += 1
    
    i = 0
    for j in range(maxx-minn+1):
        while count[j] > 0:
            arr[i] = j + minn
            i += 1
            count[j] -= 1
    
    return arr

arr = [1,0,-2,3,0,1,-1,-2,5]
print(csort(arr))