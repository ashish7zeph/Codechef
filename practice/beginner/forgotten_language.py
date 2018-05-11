for _ in range(int(input())):
    n, k = [int(x) for x in input().split()]
    a = [x for x in input().split()]
    z = []
    for i in range(k):
        y = [x for x in input().split()]
        z += y[1: int(y[0])+1]
    for i in range(n):
        if a[i] in z: print('YES', end = ' ')
        else: print('NO', end = ' ')
    print()
