a, b = map(int, input().split())

if a > b:
    horas = (24 - a) + b

elif b > a:
    horas = b - a

else:
    horas = 24

print('O JOGO DUROU %d HORA(S)' % (horas))
