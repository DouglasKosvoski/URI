lista = [0] * 100

for i in range(len(lista)):

    x = float(input())

    lista[i] = x

for j in range(len(lista)):

    if lista[j] <= 10:
        print('A[%d] = %.1f' % (j, lista[j]))
    else:
        pass
