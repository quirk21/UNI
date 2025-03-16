def pair_max(arr):
    maxx = float('-inf')
    idx = 0
    for i in range(1,len(arr)):
        sum = arr[idx] + arr[i]**2
        if sum > maxx:
            maxx = sum
        if arr[idx] < arr[i]:
            idx = i
    return maxx

num = int(input())
print(pair_max(list(map(int, input().split()))))
