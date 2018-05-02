for _ in range(int(input())):
    n = int(input())
    item = [int(x) for x in input().split()]
    item.sort(reverse = True)
    c = price = 0
    for i in range(0, n, 4):
        price += item[i]
        if i+1 < n: price += item[i+1]
    print(price)
