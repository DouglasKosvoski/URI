n = int(input())

for i in range(n):

    num = int(input())

    if num < 0:
        if num % 2 == 0:
            print('EVEN NEGATIVE')
        else:
            print('ODD NEGATIVE')

    elif num == 0:
        print('NULL')

    else:
        if num % 2 == 0:
            print('EVEN POSITIVE')
        else:
            print('ODD POSITIVE')
