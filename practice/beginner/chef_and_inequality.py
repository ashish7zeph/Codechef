t = int(input())

for i in range(t):
    a, b, c, d = [int(x) for x in input().split()]
    if a >= c:
        c += a
    if b >= d:
        b -= c
    x = (d-c+1)*(c-a)
    if c <= b:
        x += int((b-c+1)*(2*d-c-b)/2)
    print(x)
