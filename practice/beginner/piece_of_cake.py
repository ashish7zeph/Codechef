from collections import Counter
for _ in range(int(input())):
    s = input()
    l = len(s)
    s1 = Counter(s)
    flag = False
    for alpha, count in s1.items():
        if count == l - count: flag = True
    if flag: print('YES')
    else: print('NO')
