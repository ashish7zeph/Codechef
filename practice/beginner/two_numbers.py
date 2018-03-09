import math
for _ in range(int(input())):
    a, b, n = [int(x) for x in input().split()]
    a = (a * pow(2, math.ceil(n / 2) - (n // 2)))
    if  a >= b:
        x = a // b
    else:
        x = b // a
    print(x)
