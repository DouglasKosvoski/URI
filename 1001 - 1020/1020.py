age_in_days = int(input())

years  = age_in_days // 365
months = age_in_days % 365 // 30
days   = age_in_days % 365 % 30

print('{0} ano(s)'.format(years))
print('{0} mes(es)'.format(months))
print('{0} dia(s)'.format(days))
