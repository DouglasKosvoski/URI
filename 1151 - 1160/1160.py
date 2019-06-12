tests = int(input())

for i in range(tests):
    lista = list(map(float, input().split()))

    pa = lista[0]
    pb = lista[1]
    ta = 1 + (lista[2] / 100)
    tb = 1 + (lista[3] / 100)

    years = 0

    while pa <= pb:

        pa = int(pa * ta)
        pb = int(pb * tb)

        years += 1

        if years > 100:
            break

    if years <= 100:
        print(years, 'anos.')
    else:
        print('Mais de 1 seculo.')
