def csort(arr):
    max_decimal_places = max(len(str(num).split(".")[1]) if "." in str(num) else 0 for num in arr)
    scale_factor = 10 ** max_decimal_places
    arr = [int(num * scale_factor) for num in arr]
    minn = min(arr)
    maxx = max(arr)
    count = [0]*(maxx-minn+1)
    for i in arr:
        count[i-minn] += 1
    
    i = 0
    for j in range(maxx-minn+1):
        while count[j] > 0:
            arr[i] = (j + minn)/scale_factor
            i += 1
            count[j] -= 1
    
    return arr

arr = [1.5, 2.3, 0.7, 3.8, -1.2, 2.1, 3.3, -0.5, 1.8]
print(csort(arr))