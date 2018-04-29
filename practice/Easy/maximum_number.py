for _ in range(int(input())):
    n = input()
    l = len(n)
    ans = '-1'
    tot = sum(map(int, n))
    for i in range(l):
        y = n[:i] + n[i+1:]
        if int(y[-1])%2 == 0 and (tot-int(n[i]))%3 == 0 and y > ans:
            ans = y
    print(ans)

