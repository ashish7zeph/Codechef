for _ in range(int(input())):
    a, b, c = [int(x) for x in input().split()]
    if (a + b + c == 180) and (a != 0 and b != 0 and c != 0):
        print('YES')
    else:
        print('NO')
