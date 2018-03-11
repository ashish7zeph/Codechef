for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    y = 0
    i = 0
    z = 0
    while(i < n - 1):
        if a[i+1] >= a[i]:
            y += 1
        else:
            z += y * (y + 1) // 2
            y = 0
        i += 1
    z += y * (y + 1) // 2
    print(n + z)
            
            
        
