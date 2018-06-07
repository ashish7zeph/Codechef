for _ in range(int(input())):
    n = int(input())
    d = input()
    if 'I' in d: print('INDIAN')
    elif 'Y' not in d: print('NOT SURE')
    else: print('NOT INDIAN')
