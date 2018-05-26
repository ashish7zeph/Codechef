for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    minn = min(l)
    print(l.index(minn)+1)
