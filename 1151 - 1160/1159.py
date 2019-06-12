while True:

    x = int(input())

    if x == 0:
        break

    else:

        total = 0
        num = x
        q = 0

        while q < 5:

            if num % 2 == 0:
                total += num
                q += 1

            else:
                pass

            num += 1

        print(total)
