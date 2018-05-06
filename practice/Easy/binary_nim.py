for _ in range(int(input())):
    n, p = input().split()
    dee = dum = 0
    for i in range(int(n)):
        s = input()
        if s[0] == '0': dee += s.count('0')
        elif s[0] == '1': dum += s.count('1')
    if dee > dum: print('Dee')
    elif dum > dee: print('Dum')
    else:
        if p == 'Dee': print('Dum')
        else: print('Dee')
