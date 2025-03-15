num = int(input())

for i in range(num):
    usr = input().split()
    if usr[2] == "+":
        print(int(usr[1]) + int(usr[3])) 
    elif usr[2] == "-":
        print(int(usr[1]) - int(usr[3]))
    elif usr[2] == "*":
        print(int(usr[1]) * int(usr[3]))
    else:
        print(int(usr[1]) / int(usr[3]))