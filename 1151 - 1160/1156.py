total = 1

n = 3
m = 2

while n <= 39:
    total += (n/m)

    n += 2
    m *= 2

print('%.2f' % (total))
