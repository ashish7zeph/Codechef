for _ in range(int(input())):

    s = input()
    l = len(s)
    temp = 0
    
    for i in range(l):
        temp = temp ^ int(s[i])
        
    if temp == 0:
        print("LOSE")
    else:
        print("WIN")
