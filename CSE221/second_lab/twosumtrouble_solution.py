input_ = list(map(int,input().split()))
num = list(map(int,input().split()))

result = -1
left = 0
right = input_[0] -1

while left < right:
    sum = num[left] + num[right]
    if sum == input_[1]:
        result = f"{left+1} {right+1}"
        break
    elif sum < input_[1]:
        left += 1
    else:
        right -= 1

print(result)