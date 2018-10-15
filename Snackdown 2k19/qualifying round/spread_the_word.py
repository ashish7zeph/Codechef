for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    day = 0
    cap = a[0]
    know = 1
    while True:
        if know >= n: break
        day += 1
        i = know
        know += cap
        cap += sum(a[i:i+cap])
    print(day)
