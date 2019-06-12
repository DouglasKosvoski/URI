n = int(input())
lista = []
x, y = 0,1


while len(lista) < n:

    lista.append(x)

    if len(lista) < n:

        lista.append(y)

    x += y
    y += x

for i in lista:
    if i == lista[-1]:
        print(i)

    else:
        print(i, end=' ')
