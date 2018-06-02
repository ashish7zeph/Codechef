for _ in range(int(input())):
    n = int(input())
    l = [int(x) for x in input().split()]
    r = [int(x) for x in input().split()]
    mx = ans = 0
    for i in range(n):
        if l[i] * r[i] > mx:
            mx = l[i] * r[i]
            ans = i
        elif l[i] * r[i] == mx:
            if r[i] > r[ans]:
                ans = i
    print(ans + 1)
