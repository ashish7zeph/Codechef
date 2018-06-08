def F(a):
    bal = max_bal = 0
    for i in range(len(a)):
        if a[i] == '(': bal += 1
        elif a[i] == ')': bal -= 1
        max_bal = max(max_bal, bal)
    return max_bal
for _ in range(int(input())):
    a = input()
    x = F(a)
    b = ('(' * x) + (')' * x)
    print(b)
