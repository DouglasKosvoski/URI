di = input().split()
day_x, hi = int(di[1]), input().split()
hour_x, min_x, sec_x = int(hi[0]), int(hi[2]), int(hi[4])

df = input().split()
day_y, hf = int(df[1]), input().split()
hour_y, min_y, sec_y = int(hf[0]), int(hf[2]), int(hf[4])

dia = day_y - day_x
hora = hour_y - hour_x
minuto = min_y - min_x
segundos = sec_y - sec_x

if hora < 0:
	hora = 24 + hora
	dia = dia - 1

if minuto < 0:
	minuto = 60 + minuto
	hora = hora - 1

if segundos < 0:
	segundos = 60 + segundos
	minuto = minuto - 1

if dia <= 0:
	dia = 0

print("%d dia(s)" % (dia))
print("%d hora(s)" % (hora))
print("%d minuto(s)" % (minuto))
print("%d segundo(s)" % (segundos))
