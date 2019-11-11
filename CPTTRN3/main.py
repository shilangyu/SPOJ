t = int(input())

for i in range(t):
    l, c = map(int, input().split(' '))
    print('*'*(1 + 3*c))
    for _ in range(l):
        print('*' + '..*'*c)
        print('*' + '..*'*c)
        print('*'*(1 + 3*c))
    if i != t-1:
        print()
