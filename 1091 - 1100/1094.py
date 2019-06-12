test_cases = int(input())

total_animals = 0
coelhos, ratos, sapos = 0, 0, 0


for i in range(test_cases):

    num, typo = input().split()
    num = int(num)

    total_animals += num

    if typo.upper() == 'C':
        coelhos += num

    elif typo.upper() == 'R':
        ratos += num

    elif typo.upper() == 'S':
        sapos += num

    percent_coelhos = (coelhos / total_animals) * 100
    percent_ratos = (ratos / total_animals) * 100
    percent_sapos = (sapos / total_animals) * 100

print('Total: %d cobaias' % (total_animals))

print('Total de coelhos: %d' % (coelhos))
print('Total de ratos: %d' % (ratos))
print('Total de sapos: %d' % (sapos))

print('Percentual de coelhos: %.2f %%' % (percent_coelhos))
print('Percentual de ratos: %.2f %%' % (percent_ratos))
print('Percentual de sapos: %.2f %%' % (percent_sapos))
