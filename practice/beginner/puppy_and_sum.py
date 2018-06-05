def _sum_(x):
    s = 0
    while(x != 0):
        s += x
        x -= 1
    return s
for _ in range(int(input())):
    d, n = [int(x) for x in input().split()]
    for i in range(d): n = _sum_(n)
    print(n)
