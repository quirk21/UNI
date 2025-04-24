usr = input().split()
num = list(map(int, input().split()))
length = 0
left = 0
temp = 0

for right in range(int(usr[0])):
    temp += num[right]

    while temp > int(usr[1]) and left <= right:
        temp -= num[left]
        left += 1
    
    length = max(length, right - left + 1)


print(length)
