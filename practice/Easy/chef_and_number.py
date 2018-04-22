n = int(input())
def S(n):
    x = 0
    while(n):
        x += n % 10
        n //= 10
    return x
count = 0
for i in range(n//3, n):
    y = S(i)
    if i + y + S(y) == n:
        count += 1
print(count)
