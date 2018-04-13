from math import ceil
for _ in range(int(input())):
    for i in range(int(input())):
        l, n, q = [int(x) for x in input().split()]
        if l == q:
            print(n // 2)
        else:
            print(ceil(n / 2))
