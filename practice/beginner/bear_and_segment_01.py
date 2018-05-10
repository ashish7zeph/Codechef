for _ in range(int(input())):
    s = input()
    f1 = f2 = 0
    flag = 'NO'
    for i in range(len(s)):
        if f1 == 0 and s[i] == '1':
            f1 = 1
            flag = 'YES'
        elif f1 == 1 and s[i] == '0': f2 = 1
        elif f2 == 1 and s[i] == '1':
            flag = 'NO'
            break
    print(flag)
