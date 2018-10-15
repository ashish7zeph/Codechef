for _ in range(int(input())):
    n, k = [int(x) for x in input().split()]
    s = [int(x) for x in input().split()]
    s.sort(reverse = True)
    x = s[k-1]
    for i in range(k, n):
        if s[i] == x: k += 1
        else: break
    print(k)
