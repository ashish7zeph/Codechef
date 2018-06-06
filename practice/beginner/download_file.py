for _ in range(int(input())):
    n, k = [int(x) for x in input().split()]
    temp = 0
    for i in range(n):
        tx, dx = [int(x) for x in input().split()]
        if k == 0: temp += tx * dx
        elif k < tx:
            temp += (tx - k) * dx
            k = 0
        elif k >= tx: k = k - tx
    print(temp)
