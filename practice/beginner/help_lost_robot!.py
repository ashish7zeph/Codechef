for _ in range(int(input())):
    x1, y1, x2, y2 = [int(x) for x in input().split()]
    if x1 != x2 and y1 != y2: print('sad')
    elif x1 == x2 and y1 < y2: print('up')
    elif x1 == x2 and y1 > y2: print('down')
    elif y1 == y2 and x1 < x2: print('right')
    elif y1 == y2 and x1 > x2: print('left')
