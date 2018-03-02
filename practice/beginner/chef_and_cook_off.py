t = int(input())

for i in range(t):
    a = [int(x) for x in input().split()]
    y = 0
    for x in a:
        if int(x) == 1:
            y += 1

    if y == 0:
        print('Beginner')
    elif y == 1:
        print('Junior Developer')
    elif y == 2:
        print('Middle Developer')
    elif y == 3:
        print('Senior Developer')
    elif y == 4:
        print('Hacker')
    elif y == 5:
        print('Jeff Dean')
