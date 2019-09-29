from math import factorial

for _ in range(int(input())):

    n, k = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]

    a.sort()
    temp = a[k-1]

    c = a.count(temp)
    c1 = a[:k].count(temp)

    print(factorial(c) // (factorial(c1) * factorial(c-c1)))

    
        
