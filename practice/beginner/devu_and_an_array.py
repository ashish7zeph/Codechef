n, q = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
a.sort()
for _ in range(q):
    t = int(input())
    if n > 1 and t >= a[0] and t <= a[n-1]:
        print('Yes')
    elif n == 1 and t == a[0]:
        print('Yes')
    else:
        print('No')
    
