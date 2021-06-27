def lin():
    print('-' * 30)


lin()
print('    Curso em Video    ')
lin()
lin()
print('    Aprenda Python')
lin()
#-------------------------------------------------------

def mensagem(msg):
    print('-' * 30)
    print(msg)
    print('-' * 30)


mensagem('    Curso em video')
mensagem('    Aprenda Python')
#--------------------------------------------------------

a = 4
b = 5
s = a + b
print(s)
a = 8
b = 9
s = a + b
print(s)
a = 2
b = 1
s = a + b
print(s)
print()

#encolhi o codigo
def soma(a, b):
    s = a + b
    print(s)


soma(4, 5)
soma(8, 9)
soma(2, 1)

def contador(* num): #o asteristico serve para desempacotar, ou seja, pegar os parametros e jogar dentro de num
    for valor in num:
        print(f'{valor} ', end='')
    print('FIM')


contador(5, 7, 3, 1, 4)
contador(8, 4, 7)


def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1


valores = [7, 2, 3, 2]
dobra(valores)
print(valores)


def soma(* valor):
    s = 0
    for num in valor:
        s += num
    print(f'somando os {valor} temos {s}')

soma(5, 2)
soma(2, 9, 4)
