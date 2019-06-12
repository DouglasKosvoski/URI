positives = 0
average = 0

for i in range(6):
    num = float(input())
    if num > 0:
        positives += 1
        average += num

print('{0} valores positivos'.format(positives))
print('%.1f' % (average / positives))
