for _ in range(int(input())):
    s = input()
    print(sum(int(x) for x in s if x.isdigit()))
