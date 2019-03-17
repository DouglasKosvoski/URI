value = int(input())
print(value)

if 0 < value < 1000000:
    a = value // 100
    print('{0} nota(s) de R$ 100,00'.format(a))

    a = value % 100
    b = a // 50
    print('{0} nota(s) de R$ 50,00'.format(b))

    b = a % 50
    a = b // 20
    print('{0} nota(s) de R$ 20,00'.format(a))

    a = b % 20
    b = a // 10
    print('{0} nota(s) de R$ 10,00'.format(b))

    b = a % 10
    a = b // 5
    print('{0} nota(s) de R$ 5,00'.format(a))

    a = b % 5
    b = a // 2
    print('{0} nota(s) de R$ 2,00'.format(b))

    b = a % 2
    a = b // 1
    print('{0} nota(s) de R$ 1,00'.format(a))
