# Accepted

salary = float(input())

if 0 < salary and salary <= 2000:
	print("Isento")

elif 2000 < salary and salary <= 3000:
    salary -= 2000
    result = salary * 0.08
    print("R$ %.2f" % (result))

elif 3000 < salary and salary < 4500:
    salary -= 3000
    result = (salary * 0.18) + (1000 * 0.08)
    print("R$ %.2f" % (result))

else:
    salary -= 4500
    result = (salary * 0.28) + (1500 * 0.18) + (1000 * 0.08)
    print("R$ %.2f" % (result))
