CODE1, UNITS1, PRICE_UNIT1 = map(float, input().split())
CODE2, UNITS2, PRICE_UNIT2 = map(float, input().split())

CODE1, UNITS1 = int(CODE1), int(UNITS1)
CODE2, UNITS2 = int(CODE2), int(UNITS2)

PAY = (UNITS1 * PRICE_UNIT1) + (UNITS2 * PRICE_UNIT2)

print('VALOR A PAGAR: R$ %.2f'%(PAY))
