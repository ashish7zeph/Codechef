from math import gcd
for _ in range(int(input())):
    a, b = [int(x) for x in input().split()]
    print((a*b)//(gcd(a, b)**2))
