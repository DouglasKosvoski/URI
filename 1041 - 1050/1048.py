# Accepted

salary = float(input())

if salary <= 400:
    percentual = 15
elif 400 < salary <= 800:
    percentual = 12
elif 800 < salary <= 1200:
    percentual = 10
elif 1200 < salary <= 2000:
    percentual = 7
elif salary > 2000:
    percentual = 4

new_salary = salary + ((salary * percentual) / 100)
earned = new_salary - salary

print('Novo salario: %.2f' % (new_salary))
print('Reajuste ganho: %.2f' % (earned))
print('Em percentual: {0} %'.format(percentual))
