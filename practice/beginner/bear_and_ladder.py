for _ in range(int(input())):
    a, b = [int(x) for x in input().split()]
    c = 0
    if min(a, b) % 2 != 0:
        i = (min(a, b) - 1) / 2
        if max(a, b) == (2*i + 2) or max(a, b) == (2*i + 3):
            c = 1
    elif min(a, b) % 2 == 0:
        i = min(a, b) / 2
        if max(a, b) == (2*i + 2):
            c = 1
    if c == 1:
        print('YES')
    else:
        print('NO')
