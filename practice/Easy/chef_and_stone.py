for _ in range(int(input())):
    n, k = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    maxpft = 0
    for i in range(n):
        temp = k // a[i]
        temp2 = temp * b[i]
        if temp2 > maxpft:
            maxpft = temp2
    print(maxpft)
