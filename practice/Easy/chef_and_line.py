for _ in range(int(input())):
    n, k, b = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    a.sort()
    count = 1
    y = k*a[0] + b
    for i in range(1, n):
        if y <= a[i]:
            y = k*a[i] + b
            count += 1
    print(count)
        
