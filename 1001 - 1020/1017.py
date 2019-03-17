car = 12 # km/l

hours = int(input())
avrg_speed = int(input())
litters = (hours * avrg_speed) / car

print('%.3f'%(litters))
