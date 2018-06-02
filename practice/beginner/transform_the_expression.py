for _ in range(int(input())):
    s = input()
    stack = []
    temp = []
    for i in range(len(s)):
        if s[i] == '(':
            stack.append('(')
        elif s[i] >= 'a' and s[i] <= 'z': temp.append(s[i])
        elif s[i] == ')':
            while(True):
                if stack[len(stack) - 1] == '(':
                    stack.pop()
                    break
                temp.append(stack[len(stack) - 1])
                stack.pop()
        else:
            stack.append(s[i])
    print(''.join(temp))
