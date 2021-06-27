def contador (i, f, p):
    """

    :param i:  inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = 1
    while c <= f:
        print(f'{c}', end='..')
        c += p
    print('FIM')


help(contador)
#----------------------------------------------

def soma(a, b, c = 0):
    s = a + b + c
    print(f'A soma vale {s}')


soma(3, 2, 5)
soma(8, 4)

#-------------------------
#escopo de variaveis
def teste():
    x = 8
    print(f'na função teste n vale {n}')
    print(f'na função teste x vale {x}')

n = 2
print(f'no programa principal n vale {n}')
teste()
print(f'no programa principal x vale{x}') #da erro pois não ta declarado no global
#o x é variavel local e o n uma variavel global