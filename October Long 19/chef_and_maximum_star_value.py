import math
from functools import reduce

def Divisors(n):    
    return list(set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    hash_ = [0] * (max(a) + 1)

    max_ = 0
    for j in range(n):
        if hash_[a[j]] > max_:
            max_ = hash_[a[j]]
            
        divisorList = Divisors(a[j])

        for i in divisorList:
            hash_[i] += 1

    print(max_)
