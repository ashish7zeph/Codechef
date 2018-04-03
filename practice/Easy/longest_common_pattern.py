from collections import *
for _ in range(int(input())):
    a = input()
    b = input()
    count = 0
    f1 = Counter(a)
    f2 = Counter(b)
    alphabets = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    for ch in alphabets:
        if f1[ch] != 0 and f2[ch] != 0:
            if f1[ch] <= f2[ch]:
                count += f1[ch]
            else:
                count += f2[ch]
    print(count)
