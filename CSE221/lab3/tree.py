def helper(arr,left, right, new):
        if left > right:
            return 
        
        mid = (left+right)//2
        new.append(arr[mid])
        helper(arr,left,mid-1,new)
        helper(arr,mid+1,right,new)
        return new
num = int(input())
arr = list(map(int, input().split()))
new = helper(arr, 0, num-1, [])
for i in new:
      print(i, end=" ")