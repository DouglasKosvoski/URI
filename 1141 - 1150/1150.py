x = int(input())
y, soma, nums = 0, x, 1


while True:
    y = int(input())

    if y > x :
        break
    else:
        pass

while soma < y:
    soma += x + nums
    nums += 1

print(nums)
