for _ in range(int(input())):
    x, y, k, n = [int(x) for x in input().split()]
    flag = 0
    for i in range(n):
        p, c = [int(x) for x in input().split()]
        if c <= k and p >= (x - y):
            flag = 1
    if flag == 1: print('LuckyChef')
    else: print('UnluckyChef')
