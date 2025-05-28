def sort2(arr):
    i = 1
    j = len(arr)-2
    new = []
    while i < len(arr) and j > -1:
        if arr[i] > arr[j]:
            new.append(arr[j])
            j -= 2
        else:
            new.append(arr[i])
            i += 2

    while i < len(arr):
        new.append(arr[i])
        i += 2
    while j > -1:
        new.append(arr[j])
        j -= 2
    return new

arr = [23,2,19,3,7,11,5,13]
print(sort2(arr))