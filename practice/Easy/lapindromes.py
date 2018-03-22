import math
for _ in range(int(input())):
    s = input()
    x = int(len(s) / 2)
    y = math.ceil(len(s) / 2)
    a = list(s[:x])
    b = list(s[y:])
    a.sort()
    b.sort()
    if a == b:
        print('YES')
    else:
        print('NO')
