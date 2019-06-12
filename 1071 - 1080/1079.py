n = int(input())

for i in range(n):

    a, b, c = map(float, input().split())
    a, b, c = (a * 2), (b * 3), (c * 5)

    avrg = (a + b + c) / 10

    print('%.1f' % (avrg))
