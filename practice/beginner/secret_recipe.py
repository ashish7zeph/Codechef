from math import fabs
for _ in range(int(input())):
    a = [int(x) for x in input().split()]
    t1 = fabs(a[0] - a[2]) / a[3]
    t2 = fabs(a[1] - a[2]) / a[4]
    if t1 == t2: print('Draw')
    elif t1 < t2: print('Chef')
    else: print('Kefa')
