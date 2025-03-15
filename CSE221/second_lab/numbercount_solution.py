def left_binary(arr, num: int) -> int:
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low+high) // 2
        if arr[mid] >= num:
            high = mid - 1
        else:
            low = mid + 1
    return low

def right_binary(arr, num: int) -> int:
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low+high) // 2
        if arr[mid] > num:
            high = mid - 1
        else:
            low = mid + 1
    return low

def count_num(pair_num, arr):
    for i in range(pair_num):
        pair = input().split()
        print(-left_binary(arr, int(pair[0])) + right_binary(arr, int(pair[1])))


num = input().split()
arr = list(map(int, input().split()))
count_num(int(num[1]), arr)