from math import fabs
for _ in range(int(input())):
    n, m = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    mx = max(a)
    mn = min(a)
    for i in range(n):
        x = fabs(mx - i)
        y = fabs(mn - i)
        if x > y: print(int(x), end = ' ')
        else: print(int(y), end = ' ')
    print()
