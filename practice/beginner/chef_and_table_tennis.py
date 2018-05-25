for _ in range(int(input())):
    s = input()
    p1 = s.count('1')
    p2 = s.count('0')
    if p1 >= 11 and p2 < 10: print('WON')
    elif p1 >= 10 and p2 >= 10 and p1 - p2 >= 2: print('WIN')
    else: print('LOSE')
