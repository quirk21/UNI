len1 = int(input())
num1 = input().split()
len2 = int(input())
num2 = input().split()
result = []

first, second = 0, 0 
while first < len1 and second < len2:
    if int(num1[first]) <= int(num2[second]):
        result.append(num1[first])
        first += 1
    else:
        result.append(num2[second])
        second += 1

remain = (num1, first) if first < len1 else (num2, second)
print(" ".join(result), " ".join(remain[0][remain[1]:]))

# without result var (    takes more time :(    )
# remain = (num1, first, len1) if first < second else (num2, second, len2)
# print(" ".join(num1[len1:]), " ".join(remain[0][remain[1]:remain[2]]))