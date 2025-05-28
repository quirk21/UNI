# this func will return the number and number of times it appears
def binary(arr: list, num: int, leftsearch: bool) -> tuple: 
    left, right = 0, len(arr) - 1
    idx = 0
    while left <= right:
        mid = (left + right)//2
        if arr[mid] == num:
            idx = mid 
            if leftsearch:       # here the leftsearch determines which way the search will go
                right = mid - 1
            else:
                left = mid + 1
        elif arr[mid] > num:
            right = mid - 1
        else:
            left = mid + 1
    return idx

arr = list(map(int, input().split()))
num = int(input())
left = binary(arr, num, True)
right = binary(arr, num, False)
print(left, right-left+1)