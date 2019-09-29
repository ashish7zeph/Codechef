for _ in range(int(input())):
    n, k = [int(x) for x in input().split()]

    if (n % (k*k)) == 0  or k == 1:
        print("NO")
    else:
        print("YES")
