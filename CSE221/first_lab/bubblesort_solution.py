def bubbleSort(arr):                                                    
    for i in range(len(arr)-1):
        swap = False
        for j in range(len(arr)-i-1): 
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap = True
        
        if not swap:
            break
    return arr

num = input()
arr = bubbleSort(list(map(int, input().split())))
for i in arr:
    print(i,end= " ")



