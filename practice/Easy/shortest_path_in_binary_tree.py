for _ in range(int(input())):
    i, j = [int(x) for x in input().split()]
    count = 0
    while(i != j):
        if i > j:
            i //= 2
            count += 1
        elif i < j:
            j //= 2
            count += 1
    print(count)
        
