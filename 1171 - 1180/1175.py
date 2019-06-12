lista = []

for i in range(20):
    n = int(input())
    lista.append(n)

lista.reverse()

for i in range(len(lista)):
    print('N[{0}] = {1}'.format(i, lista[i]))
