a, b, c = map(float, input().split())

lista = [a, b, c]
lista.sort()

if lista[0] + lista[1] > lista[2]:
    perimeter = sum(lista)
    print('Perimetro = %.1f' % (perimeter))

else:
    area = ((a + b) * c) / 2
    print('Area = %.1f' % (area))
