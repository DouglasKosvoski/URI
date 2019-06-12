alcohol  = 0
gasoline = 0
diesel = 0

while True:

    n = int(input())

    if n in range(1, 4):
        if n == 1:
            alcohol += 1

        elif n == 2:
            gasoline += 1

        elif n == 3:
            diesel += 1


    elif n == 4:
        break

print('MUITO OBRIGADO')
print('Alcool: %d' % (alcohol))
print('Gasolina: %d' % (gasoline))
print('Diesel: %d' % (diesel))
