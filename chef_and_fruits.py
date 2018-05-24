from math import fabs
for _ in range(int(input())):
    n, m, k = [int(x) for x in input().split()]
    diff = fabs(n - m)
    if diff > k: print(int(diff - k))
    else: print(0)
