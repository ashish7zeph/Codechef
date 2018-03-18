def x(y, z, s, a):
    y = str(y)
    if y in s:
        for i in range(z, 10):
            if (str(i) in s):
                if y == str(i):
                    if s.count(y) >= 2:
                        a.append(chr(int(y + str(i))))
                else:
                    a.append(chr(int(y + str(i))))
    return a
for _ in range(int(input())):
    s = input()
    a = []
    a = x(6, 5, s, a)
    a = x(7, 0, s, a)
    a = x(8, 0, s, a)
    if ('9' in s) and ('0' in s):
        a.append('Z')
    a = ''.join(a)
    print(a)
