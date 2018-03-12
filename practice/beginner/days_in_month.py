for _ in range(int(input())):
    date, day = input().split()
    date = int(date)
    lst = [4, 4, 4, 4, 4, 4, 4]
    
    def x(lst1, y1, y2):
        for i in range(y1, y2):
            lst1[i % 7] += 1
        return lst1
    
    if day == 'mon':
        y1 = 0
    elif day == 'tues':
        y1 = 1
    elif day == 'wed':
        y1 = 2
    elif day == 'thurs':
        y1 = 3
    elif day == 'fri':
        y1 = 4
    elif day == 'sat':
        y1 = 5
    elif day == 'sun':
        y1 = 6
        
    lst = x(lst, y1, (y1 + (date % 7)))
    
    for i in range(0, 7):
        print(lst[i], end = ' ')
    print()

