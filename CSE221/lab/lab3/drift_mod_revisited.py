import sys

def mod_sum(a, n, m):
    if a == 1:
        return n % m
    mod = m * (a - 1)
    temp = pow(a, n + 1, mod)
    sum = ((temp - a) % mod) // (a - 1)
    return sum % m

def mod():
    input = sys.stdin.read
    data = input().split()
    temp = int(data[0])
    i = 1
    result = []
    
    for j in range(temp):
        a = int(data[i])
        n = int(data[i + 1])
        m = int(data[i + 2])
        i += 3
        res = mod_sum(a, n, m)
        result.append(res)
    
    for result in result:
        print(result)

mod()