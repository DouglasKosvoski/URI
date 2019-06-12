tests = int(input())

for i in range(tests):
    x = int(input())

    divisores = []

    j = x-1
    while j > 0:
        if x % j == 0:
            divisores.append(j)
        else:
            pass
        j -= 1

    if int(sum(divisores)) == x:
        print('{0} eh perfeito'.format(x))
    else:
        print('{0} nao eh perfeito'.format(x))
