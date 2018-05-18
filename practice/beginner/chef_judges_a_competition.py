for _ in range(int(input())):
    n = int(input())
    alice = [int(x) for x in input().split()]
    bob = [int(x) for x in input().split()]
    alice.remove(max(alice))
    bob.remove(max(bob))
    a = sum(alice)
    b = sum(bob)
    if a < b: print('Alice')
    elif a > b: print('Bob')
    else: print('Draw')
