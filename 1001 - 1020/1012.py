PI = 3.14159

A, B, C = map(float, input().split())

area_triang = (A * C) / 2
area_circle = PI * (C ** 2)
area_trapez = ((A + B) * C) / 2
area_square = B ** 2
area_rectan = A * B

print('TRIANGULO: %.3f'%(area_triang))
print('CIRCULO: %.3f'%(area_circle))
print('TRAPEZIO: %.3f'%(area_trapez))
print('QUADRADO: %.3f'%(area_square))
print('RETANGULO: %.3f'%(area_rectan))
