a = list(map(int, input().split()))
a.sort()
if a[3] / a[2] == a[1] / a[0] or a[3] / a[1] == a[2] / a[0]:
    print('Possible')
else:
    print('Impossible')
