t = int(input())

for i in range(t):
    n, k = [int(x) for x in input().split()]
    s = input()
    up = 0
    lo = 0
    for x in s:
        if x.islower():
            lo += 1
        elif x.isupper():
            up += 1
    if up <= k and lo <= k:
        print('both')
    elif up <= k:
        print('chef')
    elif lo <= k:
        print('brother')
    else:
        print('none')
