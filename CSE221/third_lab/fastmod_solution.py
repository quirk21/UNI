def fast_mod(base, power):
    if power == 0:
        return 1
    store = fast_mod(base, power//2)
    store **= 2
    store %= 107
    if power % 2 != 0:
        return (store * base)%107
    return store
 
arr = list(map(int, input().split()))
print(fast_mod(arr[0],arr[1]))

