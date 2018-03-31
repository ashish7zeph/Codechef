def prime(n):
    for i in range(2, n):
        if n % i == 0:
            return 0
    return 1
for _ in range(int(input())):
    x, y = [int(x) for x in input().split()]
    z = 0
    k = x + y + 1
    while(z == 0):
        if prime(k):
            print(k - x - y)
            z = 1
        k += 1
