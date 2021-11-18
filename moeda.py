#Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(),
# diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.

def aumentar(n=0, taxa=0, formato=False):
    return n * (1 + (taxa/100)) if formato is False else moeda(n * (1 + (taxa/100)))


def diminuir(n=0, taxa=0, formato=False):
    return n * (1 - (taxa/100)) if formato is False else moeda(n * (1 - (taxa/100)))


def dobro(n=0, formato=False):
    return n * 2 if formato is False else moeda(n * 2)


def metade(n=0, formato=False):
    return n / 2 if formato is False else moeda(n / 2)


def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')


def resumo(n=0, taxaa=10, taxar=5):
    print('-' * 30)
    print('Resumo do valor'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(n)}')
    print(f'Dobro do preço: \t{dobro(n, True)}')
    print(f'Metade do preço: \t{metade(n, True)}')
    print(f'Com {taxaa}% de aumento: {aumentar(n, taxaa, True)}')
    print(f'Com {taxar}% de redução: \t{diminuir(n, taxar, True)}')