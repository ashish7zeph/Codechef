for _ in range(int(input())):
    
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    x = k
    if k > n * 3:
        x = k % (n * 3)
        if x < n: x += n * 3
        
    for i in range(x):
        a[i % n] ^= a[n - i%n - 1]
        
    for i in range(n): print(a[i], end = ' ')
