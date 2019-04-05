# accepted

n1, n2, n3, n4 = map(float, input().split())

media = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / 10


if media >= 7:
    print("Media: %0.1f" % (media))
    print("Aluno aprovado.")

elif media >= 5:
    print("Media: %0.1f" % (media))
    print("Aluno em exame.")

    exame = input()
    exame = float(exame)

    media_final = (media + exame) / 2

    if media_final >= 5:
      print("Nota do exame: %0.1f" % (exame))
      print("Aluno aprovado.")
      print("Media final: %0.1f" % (media_final))

    else:
      print("Nota do exame: %0.1f" % (exame))
      print("Aluno reprovado.")
      print("Media final: %0.1f" % (media_final))

else:
  print("Media: %0.1f" % (media))
  print("Aluno reprovado.")
