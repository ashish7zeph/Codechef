for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    a.sort()
    z = 0
    for i in range(n-1, -1, -2):
        z += a[i]
    print(z)
