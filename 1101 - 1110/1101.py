while True:

    m, n = map(int, input().split())

    total = 0
    lista = [m, n]
    lista.sort()

    if m <= 0 or n <= 0:
        break

    else:
        for i in range(lista[0], lista[1]+1):
            total += i
            print(i, end=' ')

        print('Sum=%d' % (total))
