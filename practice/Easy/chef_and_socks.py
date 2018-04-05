jc, sc, m = [int(x) for x in input().split()]
if ((m - jc) // sc) % 2 != 0 or sc >= m:
    print('Unlucky Chef')
else:
    print('Lucky Chef')
