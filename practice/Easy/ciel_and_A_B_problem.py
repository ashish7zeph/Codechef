a, b = [int(x) for x in input().split()]
c = a - b
if c % 10 != 1:
    print(int(c / 10)* 10 + 1)
else:
    print(int(c / 10) * 10 + 2)
