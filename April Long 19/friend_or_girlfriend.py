for _ in range(int(input())):
    n = int(input())
    s, c = [x for x in input().split()]
    ans = 0
    k = 0
    
    for j in range(n):
        k += 1
        if s[j] == c:
            ans += (n-j) * k
            k = 0

    print(ans)
            
    
