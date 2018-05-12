for _ in range(int(input())):
    a, b, c, d = [int(x) for x in input().split()]
    ans = 0
    if a > c: c = a
    if b > d: b = d
    for i in range(a, b+1):
        if i < c: ans += (d-c+1)
        else: ans += (d-i)
    print(ans)
