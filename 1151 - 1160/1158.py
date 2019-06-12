n = int(input())

for i in range(n):
    x,y = map(int, input().split())

    nums = 0
    total = 0
    m = x

    while nums < y:

        if m % 2 != 0:
            total += m
            nums += 1

        m += 1

    print(total)
