def train (num: int) -> None:
    name = []
    destination = []
    time = []
    for i in range(num):
        detail = input().split()
        name.append(detail[0])
        destination.append(detail[4])
        time.append(detail[6])
    
    for i in range(1,num):
        j = i-1
        temp_name = name[i]
        temp_destination = destination[i]
        temp_time = time[i]
        while j>=0 and (name[j]>temp_name or (name[j] == temp_name and time[j]<temp_time)):
            name[j+1]=name[j]
            time[j+1]=time[j]
            destination[j+1]=destination[j]
            j-=1

        name[j+1]=temp_name
        time[j+1]=temp_time
        destination[j+1]=temp_destination
    
    for i in range(len(name)):
        print(f"{name[i]} will departure for {destination[i]} at {time[i]}")

num = int(input())
train(num)