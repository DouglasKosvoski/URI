while True:

    total = 0
    nums = 0

    while nums < 2:
        nota = float(input())

        if nota >= 0 and nota <= 10:
            total += nota
            nums += 1

        else:
            print("nota invalida")

    print("media = %.2f" % (total/2))

    answer = 0

    while True:
        print("novo calculo (1-sim 2-nao)")
        answer = int(input())

        if answer == 1 or answer == 2:
            break

    if answer == 2:
        break
