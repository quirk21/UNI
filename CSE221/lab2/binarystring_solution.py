num = int(input())
for i in range(num):
    binary = input()
    left = 0
    right = len(binary) - 1
    idx = -1
    while left <= right:
        mid = (left + right)//2
        if binary[mid] == '1':
            idx = mid
            right = mid - 1
        else:
            left = mid + 1

    print(idx) if idx == -1 else print(idx + 1)