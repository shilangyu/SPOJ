N = int(input())

amount = N

for i in range(2, N):
    if i*i > N:
        break
    x, y = i, i
    while x*y <= N:
        amount += 1
        y += 1

print(amount)
