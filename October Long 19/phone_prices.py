for _ in range(int(input())):

    n = int(input())
    p = [int(x) for x in input().split()]

    count = 1
    for i in range(1, n):
        if i < 5 and p[i] < min(p[:i]):
            count += 1
        elif i >= 5 and p[i] < min(p[i-5:i]):
            count += 1

    print(count)
            
