for _ in range(int(input())):
    n, k = [int(x) for x in input().split()]
    s = input()
    temp_a = y = 0
    a = s.count('a')
    for i in s:
        if i == 'a':
            temp_a += 1
        elif i == 'b':
            x = temp_a
            y += k*x + ((k*(k-1)) // 2) * a
    print(y)
