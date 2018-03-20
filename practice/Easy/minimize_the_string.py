for _ in range(int(input())):
    n = int(input())
    s = input()
    ab = ba = aa = bb = a = b = 0
    le = len(s)
    for i in range(le):
        if i < le - 1 and s[i] == 'a' and s[i+1] == 'b':
            ab += 1
        elif i < le - 1 and s[i] == 'b' and s[i+1] == 'a':
            ba += 1
        elif i < le - 1 and s[i] == 'a' and s[i+1] == 'a':
            aa += 1
        elif i < le - 1 and s[i] == 'b' and s[i+1] == 'b':
            bb += 1
        elif s[i] == 'a':
            a += 1
        elif s[i] == 'b':
            b += 1
    if ab > ba:
        r = (3 * ba - ba + 1) + (2 * (ab - ba) - 1)
    elif ba > ab:
        r = (3 * ab - ab + 1) + (2 * (ba - ab) - 1)
    elif ab == ba and ab != 0:
        r = (3 * ab - ba + 1)
    elif ab == 0 and ba == 0 and ((aa == 0 and a == 0) or (bb == 0 and b == 0)):
        r = 1
    elif ab == 0 and ba == 0:
        r = 2
    print(r)
    
    
