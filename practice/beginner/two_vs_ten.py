for _ in range(int(input())):
    x = int(input())
    count = 0
    if x % 5 != 0: print(-1)
    elif x % 10 == 0: print(0)
    else: print(1)
