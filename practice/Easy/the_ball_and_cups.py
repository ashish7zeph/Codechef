for _ in range(int(input())):
    n, c, q = [int(x) for x in input().split()]
    for i in range(q):
        l, r = [int(x) for x in input().split()]
        if c >= l and c <= r:
            c = r - (c - l)
    print(c)
