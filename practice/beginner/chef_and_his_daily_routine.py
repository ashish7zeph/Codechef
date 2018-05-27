for _ in range(int(input())):
    n = input()
    x = ['C', 'E', 'S']
    flag = True
    for i in n:
        if i not in x:
            flag = False
            break
        if i == 'E':
            if 'C' in x: x.remove('C')
        elif i == 'S':
            if 'C' in x: x.remove('C')
            if 'E' in x: x.remove('E')
    if flag: print('yes')
    else: print('no')
