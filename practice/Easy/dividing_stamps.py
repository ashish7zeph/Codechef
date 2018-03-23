n = int(input())
c = [int(x) for x in input().split()]
y = 0
for i in range(n):
    y += c[i]
if y == (n * (n + 1) // 2):
    print('YES')
else:
    print('NO')
