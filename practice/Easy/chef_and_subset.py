for _ in range(int(input())):
    a = [int(x) for x in input().split()]
    brk = 0
    for i in a:
        if brk == 1:
            break
        elif i == 0 or a[0] + a[1] + a[2] + a[3] == 0:
            brk = 1
        else:
            for j in a:
                if i + j == 0 and i != j:
                    brk = 1
                    break
    if brk != 1:
        if a[0] + a[1] + a[2] == 0 or a[1] + a[2] + a[3] == 0:
            brk = 1
        elif a[0] + a[1] + a[3] == 0 or a[0] + a[2] + a[3] == 0:
            brk = 1
    if brk == 1:
        print('Yes')
    else:
        print('No')
