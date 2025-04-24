def merge(arr1, arr2, count):
    i, j = 0, 0
    new = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] > arr2[j]:
            new.append(arr2[j])
            j += 1
            count += len(arr1) - i
        else:
            new.append(arr1[i])
            i += 1
    
    while i < len(arr1):
        new.append(arr1[i])
        i += 1
    while j < len(arr2):
        new.append(arr2[j])
        j += 1

    return new, count

def mergeSort(arr):
    count = 0
    if len(arr) <= 1:
        return arr, count
    else:
        mid = len(arr)//2
        a1, count1 = mergeSort(arr[:mid])
        a2, count2 = mergeSort(arr[mid:])  
        new, count3 = merge(a1, a2, count1+count2)  
        return new, count3
    
num = int(input())
arr = list(map(int, input().split()))
temp = mergeSort(arr)
print(temp[1])
for i in temp[0]:
    print(i, end=" ")