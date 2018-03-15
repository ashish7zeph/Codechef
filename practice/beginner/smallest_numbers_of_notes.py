for _ in range(int(input())):
    n = int(input())
    x = 0
    if n // 100 != 0:
        x += n // 100
        n = n % 100
    if n // 50 != 0:
        x += n // 50
        n = n % 50
    if n // 10 != 0:
        x += n // 10
        n = n % 10
    if n // 5 != 0:
        x += n // 5
        n = n % 5
    if n // 2 != 0:
        x += n // 2
        n = n % 2
    if n // 1 != 0:
        x += n // 1
    print(x)
