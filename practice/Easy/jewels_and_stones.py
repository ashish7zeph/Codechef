for _ in range(int(input())):
    jew = set(list(input()))
    stone = input()
    count = 0
    for i in stone:
        if i in jew:
            count += 1
    print(count) 
