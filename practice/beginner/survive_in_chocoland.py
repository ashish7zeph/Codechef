import math
for _ in range(int(input())):
    n, k, s = [int(x) for x in input().split()]
    if ((s >= 7 and (7 * k) <= 6 * n)) or (s < 7 and n >= k):
        print(math.ceil((k * s) / n))
    else:
        print(-1)
 
 
