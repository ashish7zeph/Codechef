for _ in range(int(input())):
    a, b = [int(x) for x in input().split()]
    if a > b: print('>')
    elif a < b: print('<')
    else: print('=')
