for _ in range(int(input())):
    n, m, k, l = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    first = m * l
    b = [0] * (n+1)
    temp = first
    a.sort()
    for i in range(n):
        temp += l
        b[i] = temp - a[i]
    b[n] = (temp + l) - k
    print(min(b))
