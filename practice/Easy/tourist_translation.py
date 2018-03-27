t, m = [x for x in input().split()]
t = int(t)
for _ in range(t):
    s = input()
    a = []
    for i in s:
        if i == '_':
            a.append(' ')
        elif i >= 'a' and i <= 'z':
            a.append(m[ord(i) % 97])
        elif i >= 'A' and i <= 'Z':
            a.append(m[ord(i) % 65].upper())
        else:
            a.append(i)
    print(''.join(a))
