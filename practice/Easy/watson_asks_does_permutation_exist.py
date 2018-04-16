for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    if (max(a)-min(a)) < len(set(a)):
        print('YES')
    else:
        print('NO')
