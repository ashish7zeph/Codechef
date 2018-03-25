for _ in range(int(input())):
    n = int(input())
    w = [int(x) for x in input().split()]
    c = w[n - 1]
    for i in range(n - 2, -1, -1):
        if w[i] > c:
            c = w[i]
        else:
            c += 1
    print(c)