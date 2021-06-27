'''cont = 1
while True: #nesse caso o programa pode rodar para sempre
    print(cont, '->', end='')
    cont += 1
print('acabou')'''
n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
#print('A soma vale: {}'.format(s))
print(f'a soma vale {s}')