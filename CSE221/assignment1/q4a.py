# this func will find the biggest number in a wavelike array like
# [1, 3, 4, 5, 9, 6, 2, -1]

def numwave(arr):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left+right)//2
        if (mid == 0 or arr[mid]>arr[mid-1]) and (mid == len(arr)-1 or arr[mid+1]<arr[mid]):
            return arr[mid]
        elif arr[mid] < arr[mid+1]:
            left = mid + 1
        else:
            right = mid - 1 

arr = [1, 3, 4, 5, 9, 6, 2, -1]
print(numwave(arr))                   