#Reescreva a função leiaInt() que fizemos no desafio 104, incluindo
# agora a possibilidade da digitação de um número de tipo inválido.
# Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31merro! digite um numero inteiro\033[m')
            continue #faz ir para o while de novo
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31merro! digite um numero real\033[m')
            continue #faz ir para o while de novo
        else:
            return n


num = leiaint('Digite um numero inteiro: ')
num2 = leiafloat('digite um valor real: ')
print(f'Voce acabou de digitar o numero inteiro {num}')
print(f'Voce acabou de digitar o numero real {num2}')
