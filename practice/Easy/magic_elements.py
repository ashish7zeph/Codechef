for _ in range(int(input())):
    n, k = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    s = sum(a)
    count = 0
    for i in a:
        if (i + k) > (s - i):
            count += 1
    print(count)
