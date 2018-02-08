n = int(input())
a = [int(x) for x in input().split()]

sum = 0
if n <= 1000:
    for i in range(n):
        for j in range(i+1, n):
            sum += (a[i] & a[j])
else:
    v=a.count(1)
    sum=v*(v-1)//2

print(sum)
