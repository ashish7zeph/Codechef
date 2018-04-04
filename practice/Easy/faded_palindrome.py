for _ in range(int(input())):
    s = input()
    temp = []
    l = len(s)
    
    for i in range(l):
        if s[i] == '.' and s[l-1-i] != '.' and l-1-i != i:
            temp.append(s[l-1-i])
        elif (s[i] == '.' and l-1-i == i) or (s[i] == '.' and s[l-1-i] == '.'):
            temp.append('a')
        else:
            temp.append(s[i])
    temp2 = ''.join(temp)
    
    if l % 2 == 0 and temp[:l // 2] == temp[:l // 2 - 1:-1]:
        print(temp2)
    elif l % 2 != 0 and temp[:l // 2] == temp[:l // 2:-1]:
        print(temp2)
    else:
        print(-1)
