for _ in range(int(input())):
    s = input()
    temp = []
    for i in range(len(s) - 1):
        temp.append(s[i:i+2])
    print(len(set(temp)))
