for _ in range(int(input())):
    h, cc, ts = [x for x in input().split()]
    h = int(h)
    cc = float(cc)
    ts = int(ts)
    t1 = t2 = t3 = False
    if h > 50: t1 = True
    if cc < 0.7: t2 = True
    if ts > 5600: t3 = True
    if t1 and t2 and t3: print('10')
    elif t1 and t2: print('9')
    elif t2 and t3: print('8')
    elif t1 and t3: print('7')
    elif t1 or t2 or t3: print('6')
    else: print('5')
