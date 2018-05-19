for _ in range(int(input())):
    p = int(input())
    price = 0
    ar = [1,2,4,8,16,32,64,128,256,512,1024,2048]
    for i in range(11, -1, -1):
        m = p % ar[i]
        price += p // ar[i]
        if m != 0: p = m
        elif m == 0: break
    print(price)
