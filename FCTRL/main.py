T = int(input())

for _ in range(T):
    N = int(input())
    Z = 0
    while N != 0:
        Z += N//5
        N //= 5
    print(Z)
