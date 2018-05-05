for _ in range(int(input())):
    n = int(input())
    m = [int(x) for x in input().split()]
    last = 0
    y = 0
    for i in range(n):
        if m[i] > last:
            y += m[i] - last
        last = m[i]
    print(y)
