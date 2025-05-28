# this func will give the first index of the number we want
def binary(arr: list, num: int) -> int:
    left = 0
    right = len(arr)-1
    idx = 0
    while left <= right:
        mid = (left + right)//2
        if arr[mid] == num:
            idx = mid
            right = mid - 1 
        elif arr[mid] > num:
            right = mid - 1
        else:
            left = mid + 1 
    return idx

arr = list(map(int, input().split()))
num = int(input())
print(binary(arr, num))