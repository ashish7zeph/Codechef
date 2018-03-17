for i in range(input().split()):
    n = int(input())
    a = [int(x) for x in input().split()]
    k = int(input())
    temp = a[k-1]
    a.sort()
    for j in range(n):
        if a[j] == temp:
            print(j+1)
            break
