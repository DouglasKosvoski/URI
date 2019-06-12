soma, nums = 0, 0

while nums < 2:
    nota = float(input())

    if nota >= 0 and nota <= 10:
        soma += nota
        nums += 1

    else:
        print("nota invalida")

print("media = %.2f" % (soma/nums))
