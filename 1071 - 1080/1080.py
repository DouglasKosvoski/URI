highest = 0
lista = {}

for i in range(100):

    valor = int(input())

    if valor > highest:
        highest = valor
        lista[valor] = i

print(highest)
print(lista[highest]+1)
