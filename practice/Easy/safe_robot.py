for _ in range(int(input())):
    n, m = map(int, input().split())
    s = input()    
    x = 0
    y = 0
    bound_y_max = 0
    bound_y_min = 0
    bound_x_max = 0
    bound_x_min = 0
    
    for i in s:
        if i == 'R':
            y += 1
            bound_y_max = max(y, bound_y_max)
        elif i == 'U':
            x -= 1
            bound_x_min = min(x, bound_x_min)
        elif i == 'L':
            y -= 1
            bound_y_min = min(y, bound_y_min)
        else:
            x += 1
            bound_x_max = max(x, bound_x_max)
 
    aa = bound_y_max - bound_y_min + 1
    bb = bound_x_max - bound_x_min + 1
 
    if aa <= m and bb <= n:
        print('safe')
    else:
        print('unsafe')
                 
   
