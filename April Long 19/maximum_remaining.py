n = int(input())
a = {int(x) for x in input().split()}
a = list(a)
if len(a) == 1: print(0)
else:
    m = a.index(max(a))
    a.pop(m)
    print(max(a))
