t = int(input())

for i in range(t):
    y = 1
    n, q = [int(x) for x in input().split()]
    d = [int(x) for x in input().split()]
    for x in d:
        y *= int(x)
    queries = [int(x) for x in input().split()]
    for x in queries:
        print(int(int(x) / y), end = ' ')
    print()
