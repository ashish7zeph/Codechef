for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    a.sort()
    y = 0
    z = 0
    x = 0
    for i in range(n-1, 0, -1):
        if a[i - 1] == a[i] and a[i] > y:
            y = a[i]
            a.remove(a[i])
            a.remove(a[i-1])
            x += 2
            break
    for i in range(n-1-x, 0, -1):
        if a[i - 1] == a[i] and a[i] > z:
            z = a[i]
            break
    if y != 0 and z != 0:
        print(y * z)
    else:
        print(-1)
            
