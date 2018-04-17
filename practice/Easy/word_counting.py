import collections
from math import factorial
m = 10**9 + 7
for _ in range(int(input())):
    s = input()
    count = collections.Counter(s)
    y = factorial(len(s))
    x = 1
    for i in count.values():
        if i > 1: x *= factorial(i)
    print((y // x) % m)
