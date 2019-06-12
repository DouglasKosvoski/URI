inter_goals, gremio_goals = map(int, input().split())
grenais = 1

inter_victories  = 0
gremio_victories = 0
draws = 0

while True:
    print('Novo grenal (1-sim 2-nao)')
    answer = int(input())

    # WHO WON?
    if inter_goals > gremio_goals:
        inter_victories += 1

    elif gremio_goals > inter_goals:
        gremio_victories += 1

    else:
        draws += 1


    # CONTINUE THE PROGRAM?
    if answer == 1:
        inter_goals, gremio_goals = map(int, input().split())
        grenais += 1

    else:
        break



print('%d grenais' % (grenais))
print('Inter:%d' % (inter_victories))
print('Gremio:%d' % (gremio_victories))
print('Empates:%d' % (draws))

if inter_victories > gremio_victories:
    print('Inter venceu mais')

elif inter_victories < gremio_victories:
    print('Gremio venceu mais')
