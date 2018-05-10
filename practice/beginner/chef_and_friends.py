count = 0
for _ in range(int(input())):
    u = input()
    if ('ch' in u) or ('he' in u) or ('ef' in u): count += 1
print(count)
