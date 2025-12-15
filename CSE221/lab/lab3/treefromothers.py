def truetree(inorder, preorder, new):
    if not inorder:
        return 
    
    temp = preorder[0]
    mid = inorder.index(temp)
    
    truetree(inorder[:mid],preorder[1:mid+1],new)
    truetree(inorder[mid+1:],preorder[mid+1:],new)
    new.append(temp)
    return new
num = int(input())
inorder = list(map(int, input().split()))
preorder = list(map(int, input().split()))
tree = truetree(inorder, preorder,[])
for i in tree:
    print(i, end=" ")