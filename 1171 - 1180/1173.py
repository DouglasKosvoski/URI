lista = [0] * 10
n = int(input())

for i in range(1, 10+1):

    lista[i-1] = n
    n = lista[i-1] * 2


for j in range(len(lista)):
    print('N[{0}] = {1}'.format(j, lista[j]))
