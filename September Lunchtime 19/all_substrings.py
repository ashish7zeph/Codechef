for _ in range(int(input())):

    s = input()
    r = input()

    temp = [0] * (26)
    flag = 1
    for i in r:
        temp[ord(i) - 97] += 1

    for i in s:
        if temp[ord(i) - 97] == 0:
            flag = 0
            break
        temp[ord(i) - 97] -= 1

    if flag:
        s1 = ""
        for i in range(26):
            for j in range(temp[i]):
                s1 += chr(i + 97)

        l = len(s1)
        if l == 0:
            print(s)
        for i in range(l):
            if s[0] == s1[i] and s < s1[i]*len(s):
                print(s1[:i] + s + s1[i:])
                break
            elif s[0] < s1[i]:
                print(s1[:i] + s + s1[i:])
                break
            elif i == l-1:
                print(s1 + s)

    else:
        print('Impossible')
            
