def maxpair(arr):
    


num = int(input())
arr = list(map(int, input().split()))
temp = maxpair(arr)
print(temp[-1]**2+temp[-2])
