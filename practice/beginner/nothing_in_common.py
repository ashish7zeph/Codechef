for _ in range(int(input())):
    n, m = [int(x) for x in input().split()]
    a = {int(x) for x in input().split()}
    b = {int(x) for x in input().split()}
    c = set(list(a) + list(b))
    print(m + n - ((n - len(a)) + (m - len(b)) + len(c)))
