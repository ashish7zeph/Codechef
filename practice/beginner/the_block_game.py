for _ in range(int(input())):
    n = list(input())
    if n[::-1] == n: print('wins')
    else: print('losses')
