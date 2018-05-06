for _ in range(int(input())):
    h, s = [int(x) for x in input().split()]
    if h*h < 4*s: print(-1)
    else:
        p = ((h*h + 4*s)**0.5 + (h*h - 4*s)**0.5) / 2
        b = ((h*h + 4*s)**0.5 - (h*h - 4*s)**0.5) / 2
        print("{0:.6f}".format(b), end = ' ')
        print("{0:.6f}".format(p), end = ' ')
        print("{0:.6f}".format(h))
