num = input()
id = list(map(int,input().split()))
mark = list(map(int,input().split()))
new = []
swap = 0

for i in range(len(mark)):
    max = i

    for j in range(i+1, len(mark)):
        if mark[max] < mark[j]:
            max = j

        elif mark[max] == mark[j] and id[max] > id[j]:
            max = j
            
    if i != max:            
        mark[i], mark[max] = mark[max], mark[i]
        id[i], id[max] = id[max], id[i]
        swap += 1
    

print("Minimum swaps: ",swap)
for i in range(len(mark)):
     print(f"ID: {id[i]} Mark: {mark[i]}")
