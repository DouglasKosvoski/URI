evens = 0

for i in range(5):
    num = int(input())
    if num % 2 == 0:
        evens += 1

print('{0} valores pares'.format(evens))
