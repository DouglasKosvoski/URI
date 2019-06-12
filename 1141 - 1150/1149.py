lista = list(map(int,input().split()))

n1 = lista[0]
n2 = lista[-1]

soma = 0
for i in range(0, n2):
    soma += n1 + i

print(soma)
