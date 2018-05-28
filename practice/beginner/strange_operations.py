for _ in range(int(input())):
    n, k = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    s = sum(a)
    if s % 2 and k == 1: print('odd')
    else: print('even')
