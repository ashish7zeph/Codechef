for _ in range(int(input())):
    n = int(input())
    a = []
    for i in range(n):
        if n > 2 and n % 2 != 0 and i == n-1: a.append(i+1)
        elif i % 2 == 0: a.append(i+2)
        elif i % 2 != 0: a.append(i)
    if n > 2 and n % 2 != 0:
        temp = a[n-1]
        a[n-1] = a[n-2]
        a[n-2] = temp
    for i in range(n): print(a[i], end = ' ')
    print()
