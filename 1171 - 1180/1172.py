lista = []

for i in range(10):

    x = int(input())

    if x <= 0:
        lista.append(1)
    else:
        lista.append(x)

for j in range(len(lista)):

    print('X[{0}] = {1}'.format(j, lista[j]))
