for _ in range(int(input())):
    n, m = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]

    temp = [0] * (n+1)
    flag = 1
    for i in range(m):
        temp[a[i]] += 1
        if abs(min(temp[1:]) - temp[a[i]]) > 1:
            flag = 0
            break
        
    if flag:
        print('YES')
    else:
        print('NO')
