A, B, C = map(float, input().split())

lados = [A, B, C]
lados.sort()

if lados[2] >= lados[0] + lados[1]:
    print('NAO FORMA TRIANGULO')

else:
    if lados[2]**2 == lados[0]**2 + (lados[1]**2):
        print('TRIANGULO RETANGULO')

    if lados[2]**2 > lados[0]**2 + (lados[1]**2):
        print('TRIANGULO OBTUSANGULO')

    if lados[2]**2 < lados[0]**2 + (lados[1]**2):
        print('TRIANGULO ACUTANGULO')

    if lados[0] == lados[1] and lados[0] == lados[2]:
        print('TRIANGULO EQUILATERO')

    elif lados[0] == lados[1] or lados[2] == lados[1] or lados[0] == lados[2]:
        print('TRIANGULO ISOSCELES')
