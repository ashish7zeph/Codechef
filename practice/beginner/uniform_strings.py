t = int(input())

for i in range(t):
    s = input()
    x = 0
    for j in range(7):
        if s[j+1] != s[j]:
            x += 1
    if s[7] != s[0]:
        x += 1

    if x <= 2:
        print('uniform')
    else:
        print('non-uniform')
