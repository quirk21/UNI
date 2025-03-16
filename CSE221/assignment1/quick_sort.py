def quicksort(arr: list, left: int, right: int) -> list:
    if left < right:
        idx = partition(arr, left, right)
        quicksort(arr, left, idx-1)
        quicksort(arr, idx+1, right)
        return arr
    else:
        return arr

def partition(arr, left, right):
    i, j = left, right
    pivot = arr[left]
    while i < j:
        while i < right and arr[i] <= pivot:
            i += 1
        while j > left and arr[j] > pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[left], arr[j] = arr[j], arr[left]
    return j

arr = [ 1,2,11,5,6,10,9,1,0,5]
print(quicksort(arr,0,len(arr)-1))
