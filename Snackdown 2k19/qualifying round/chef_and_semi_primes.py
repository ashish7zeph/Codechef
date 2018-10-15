import math

prime = [False]*201
semiPrime = []

def isprime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0: return False
    return True

for i in range(2, 201):
    prime[i] = isprime(i)

for i in range(2, 201):
    for j in range(i+1, 201):
        if prime[i] and prime[j]:
            semiPrime.append((i) * (j))
l = len(semiPrime)

for _ in range(int(input())):
    n = int(input())
    flag = False
    for i in range(l):
        for j in range(l):
            if semiPrime[i] + semiPrime[j] == n:
                flag = True
                break
        if flag: break
    if flag: print('YES')
    else: print('NO')
