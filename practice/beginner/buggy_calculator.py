for _ in range(int(input())):
    a, b = [int(x) for x in input().split()]
    c = 1
    x = 0
    while(a or b):
       temp = (a%10 + b%10) % 10
       b = b//10
       a = a//10
       x += temp * (c)
       c *= 10
    print(x)
           
        
