for _ in range(int(input())):

    n = int(input())

    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]

    mx = 0
    for i in range(n):

        res = a[i] * 20 - b[i] * 10

        if res > mx:
            mx = res

    print(mx)
