n = int(input())

a, b, c = 1, 1, 1

for i in range(n):

    print(a, b, c)

    a = a + 1
    b = a ** 2
    c = a ** 3
