from math import ceil

k = 1

while 1:
    stack = 0
    N = 0
    s = input().strip()
    if s[0] == '-':
        break
    for char in s:
        if char == '{':
            stack += 1
        else:
            if stack == 0:
                stack += 1
                N += 1
            else:
                stack -= 1
    N += ceil(stack/2)
    print(f'{k}. {N}')
    k += 1
