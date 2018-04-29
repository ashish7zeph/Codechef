for _ in range(int(input())):
    a, b = [x for x in input().split()]
    ab = a + b
    c = 0
    x = ''
    for i in range(int(input())):
        x += input()
    z = set(x)
    for i in z:
        if ab.count(i) >= x.count(i):
            c += 1
    if c == len(z):
        print('YES')
    else:
        print('NO')
