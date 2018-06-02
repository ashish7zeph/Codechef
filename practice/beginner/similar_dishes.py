for _ in range(int(input())):
    ing1 = input().split()
    ing2 = input().split()
    count = 0
    for ing in ing1:
        if ing in ing2: count += 1
    if count >= 2: print('similar')
    else: print('dissimilar')
