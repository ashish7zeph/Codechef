for _ in range(int(input())):
    n = int(input())
    a = []
    
    for i in range(n):
        s = input()
        a.append(s.split(' ', 1))
        
    for i in range(n):
        if i == 0:
            print('Begin ' + a[n-1][1])
        else:
            if a[n-i][0] == 'Right':
                print('Left ' + a[n-1-i][1])
            elif a[n-i][0] == 'Left':
                print('Right ' + a[n-1-i][1])
    print()
