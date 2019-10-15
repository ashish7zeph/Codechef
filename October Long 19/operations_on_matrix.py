for _ in range(int(input())):
    
    x1, y1, d = map(int,input().split())
    h1 = [0] * x1
    h2 = [0] * y1
    
    while(d):
        a, b = map(int,input().split())
        h1[a-1] += 1
        h2[b-1] += 1
        d -= 1
        
    count = 0
    even1 = 0
    even2 = 0
    for i in h1:
        if(i % 2 == 0):
            even1 += 1
    for j in h2:
        if(j % 2 == 0):
            even2 += 1
            
    count += (even1 * even2)
    count += (x1 - even1) * (y1 - even2)
    
    print(count)
