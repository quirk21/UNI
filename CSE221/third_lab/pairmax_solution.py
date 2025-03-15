def merge(arr1, arr2):
    i, j = 0, 0
    new = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] > arr2[j]:
            new.append(arr2[j])
            j += 1
        else:
            new.append(arr1[i])
            i += 1
    
    while i < len(arr1):
        new.append(arr1[i])
        i += 1
    while j < len(arr2):
        new.append(arr2[j])
        j += 1

    return new

def mergeSort(arr):
    count = 0
    if len(arr) <= 1:
        return arr, count
    else:
        mid = len(arr)//2
        a1 = mergeSort(arr[:mid])
        a2 = (arr[mid:])  
        new = merge(a1, a2)  
        return new
    
num = int(input())
arr = list(map(int, input().split()))
temp = mergeSort(arr)
print(temp[-1]**2+temp[-2])
