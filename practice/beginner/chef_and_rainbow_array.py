import math
for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    x = int(n / 2)
    y = math.ceil(n / 2)
    b = a[:x]
    c = a[y:]
    c.reverse()
    if b == c and n >= 13 and list(set(a)) == [1,2,3,4,5,6,7]:
        if n % 2 == 0:
            print('yes')
        elif n % 2 != 0 and a[int(n/2)] == 7:
            print('yes')
        else:
            print('no')
    else:
        print('no')
