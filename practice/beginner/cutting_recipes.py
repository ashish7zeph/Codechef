for _ in range(int(input())):
    x = [int(x) for x in input().split()]
    y = x[1:]
    mn = min(y)
    while(mn):
        flag = True
        for i in y:
            if i % mn != 0:
                flag = False
                break
        if flag:
            z = [str(x // mn) for x in y]
            break
        else: mn -= 1
    print(' '.join(z))
