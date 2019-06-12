n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    odds = 0

    for j in range(min(x,y)+1, max(x,y)):

        if j % 2 != 0:
            odds += j

    print(odds)
