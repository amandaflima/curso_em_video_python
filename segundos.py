seg = int(input('entre com a quantidade de segundos que quer converter: '))
dias = seg // 86400
horas = (seg % 86400) // 3600
min = (seg % 3600) // 60
s = seg % 60
print(f'{dias} dias, {horas} horas, {min} minutos, {s} segundos')