total = 0
nums = 0


while True:

	x = int(input())

	if x > -1:
		total += x
		nums += 1
	else:
		break

print('%.2f' % (total/nums))
