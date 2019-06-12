n = int(input())

for j in range(n):
    x = int(input())
    divs = 0

    for i in range(2,x):
        if x % i == 0:
            divs += 1
            break

    if divs == 0: print(x, 'eh primo')
    else: print(x, 'nao eh primo')
