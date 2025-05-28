def csort(arr, max):
    new = [0]*(max+1)
    for i in range(len(arr)):
        new[arr[i]] += 1
    i = 0
    for j in range(max+1):
        while new[j] > 0:
            arr[i] = j
            i += 1
            new[j] -= 1
    return arr
arr = [9,8,7,6,5,5,5,4,4,3,2,2,1,1]
print(csort(arr,9))
print("===========================")
print()
def csort2(arr, max):
    count = [0]*(max+1)
    new = [0]*len(arr)
    for i in range(len(arr)):
        count[arr[i]] += 1
    for i in range(1, len(count)):
        count[i] = count[i] + count[i-1]
    
    for i in range(len(arr) - 1, -1, -1):
        new[count[arr[i]]-1]  = arr[i]
        count[arr[i]] -= 1
    return new
arr = [9,8,7,6,5,5,5,4,4,3,2,2,1,1]
print(csort2(arr,9))      