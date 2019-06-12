evens, odds, positives, negatives = 0,0,0,0

for i in range(5):
    num = int(input())

    if num > 0:
        positives += 1
    elif num < 0:
        negatives += 1

    if num % 2 == 0:
        evens += 1
    else:
        odds += 1

print('{0} valor(es) par(es)'.format(evens))
print('{0} valor(es) impar(es)'.format(odds))
print('{0} valor(es) positivo(s)'.format(positives))
print('{0} valor(es) negativo(s)'.format(negatives))
