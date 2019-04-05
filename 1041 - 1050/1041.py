# accepted

x, y = map(float, input().split())

def quadrant():

    if x != 0 and y != 0:
        if x < 0:
            if y > 0:
                print('Q2')
            else:
                print('Q3')

        elif x > 0:
            if y > 0:
                print('Q1')
            else:
                print('Q4')

    else:
        if y == 0 and x != 0:
            print('Eixo X')
        elif x == 0 and y != 0:
            print('Eixo Y')
        else:
            print('Origem')

quadrant()
