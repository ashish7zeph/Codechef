from math import *
for _ in range(int(input())):
    a, b, c = [int(x) for x in input().split()]
    print(int(ceil(fabs(((b - a) - (c - b)) / 2))))
