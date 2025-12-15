# union find
import sys
sys.setrecursionlimit(2**17)

# input
N, K = map(int, sys.stdin.readline().split())
par = [i for i in range(N+1)]
size = [1]*(N+1)

def find(x):
    # as the the parent of 'the parent of a set' is that number we search for it recursively
    if par[x] != x:
        # we also keep updating the parent
        par[x] = find(par[x])
    return par[x]

for _ in range(K):
    start, end = map(int, sys.stdin.readline().split())
    # finding their parent/representative
    friend1 = find(start)   
    friend2 = find(end)

    if friend1 != friend2:
        # setting friend1 as the parent of friend2
        par[friend2] = friend1  
        # removing frined2 from it's own circle because it now belongs to the circle of friend1 
        size[friend1] += size[friend2]  
        size[friend2] = 0  

    print(size[friend1])