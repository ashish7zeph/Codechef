for _ in range(int(input())):
    n, u, d = [int(x) for x in input().split()]
    h = [int(x) for x in input().split()]
    flag = 1
    temp = h[0]
    c = 1
    for i in range(1, n):
        if h[i] == temp:
            c += 1
            temp = h[i]
        elif h[i] > temp and h[i] - temp <= u:
            c += 1
            temp = h[i]
        elif h[i] < temp and temp - h[i] <= d:
            c += 1
            temp = h[i]
        elif h[i] < temp and temp - h[i] > d and flag:
            flag = 0
            c += 1
            temp = h[i]
        else:
            break
    print(c)
            
