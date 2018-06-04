for _ in range(int(input())):
    n = int(input())
    i = 0
    while(n - i > 0):
        i += 1
        n -= i
    print(i)
