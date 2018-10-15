for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    flag = 1
    for i in range(n-2):
        x = b[i] - a[i]
        if x < 0:
            flag = 0
            break
        elif x > 0:
            b[i] -= x
            b[i+1] -= 2*x
            b[i+2] -= 3*x
    if b[n-2] != a[n-2] or b[n-1] != a[n-1]: flag = 0
    if flag: print('TAK')
    else: print('NIE')
