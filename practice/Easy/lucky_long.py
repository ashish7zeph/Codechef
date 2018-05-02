for _ in range(int(input())):
    n = input().strip()
    a = n.count('4')
    b = n.count('7')
    print(len(n)-(a+b))
