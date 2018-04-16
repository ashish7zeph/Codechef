for _ in range(int(input())):
    n, k = [int(x) for x in input().split()]
    s = [int(x) for x in input().split()]
    temp = [0 for x in range(200001)]
    for i in s:
        temp[i] = 1
    if k == 0:
        for i in range(len(temp)):
            if temp[i] == 0:
                print(i)
                break
    else:
        for i in range(len(temp)):
            if temp[i] == 0 and k > 0:
                k -= 1
            elif temp[i] != 1:
                print(i)
                break
