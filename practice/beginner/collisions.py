for _ in range(int(input())):
    n, m = [int(x) for x in input().split()]
    a = []
    z = 0
    for i in range(n):
        a.append(input())
    for i in range(m):
        y = 0
        for j in range(n):
            y += int(a[j][i])
        y -= 1
        z += y * (y + 1) // 2
    print(z)
