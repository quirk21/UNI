from math import gcd

def Coprime(node, query):
    graph = [[] for _ in range(node+1)]
    for i in range(1,node+1):
        for j in range(i+1,node+1):
            if gcd(i,j)==1:
                graph[i].append(j)
                graph[j].append(i)

    arr = []
    for j in range(query):
        x, k = input().split()
        if len(graph[int(x)]) < int(k):
            arr.append(-1)
        else:
            arr.append(graph[int(x)][int(k)-1])

    for i in arr:
        print(i) 

x, y = input().split()
Coprime(int(x), int(y))
