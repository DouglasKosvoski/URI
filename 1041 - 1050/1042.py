a, b, c = map(int, input().split())

lista_original = [a, b, c]
lista_sorted = [a, b, c]

lista_sorted.sort()
for i in lista_sorted:
    print(i)

print()

for i in lista_original:
    print(i)
