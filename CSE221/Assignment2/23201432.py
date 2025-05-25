# function for eucledean distance
dist = lambda a,b: (((b[1]-a[1])**2+(b[0]-a[0])**2)**.5, a[2], b[2])

# function for closest pair
def closest_pair(x_list, y_list):
    n = len(x_list)

    # base case
    if n==2:
        return dist(x_list[0],x_list[1])
    if n==3:
        return min(dist(x_list[0],x_list[1]),dist(x_list[0],x_list[2]),dist(x_list[2],x_list[1]), key=lambda x:x[0])
    
    # divide
    mid = n//2
    left = closest_pair(x_list[:mid], y_list)
    right = closest_pair(x_list[mid:], y_list)
    minimum = min(left, right, key=lambda x:x[0])

    # combine
    y_band = [i for i in y_list if x_list[mid][0]-minimum[0] < i[0] < x_list[mid][0]+minimum[0] ]
    for i in range(len(y_band)):
        for j in range(i+1, min(i+7, len(y_band))):
            temp = dist(y_band[i], y_band[j])
            if temp[0] < minimum[0]:
                minimum = temp
    return minimum

# taking inputs
num = int(input())
x_list = []
for i in range(num):
    x_list.append((*map(int, input().split()),i+1)) # '*' to  break the map tuple
# sorting according to x co ordinate 
y_list = x_list.copy()
x_list.sort(key=lambda x:x[0])
y_list.sort(key=lambda x:x[1])

res = closest_pair(x_list, y_list)
print(res[2], res[1], res[0])
