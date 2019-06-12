n = int(input())

inn = 0
outt = 0

for i in range(n):
    num = int(input())

    if 10 <= num and num <= 20:
        inn += 1
    else:
        outt += 1

print('%d in' % (inn))
print('%d out' % (outt))
