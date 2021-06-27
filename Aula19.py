'''#lista com dicionarios

brasil = []
estado1 = {'uf': 'Rio de janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(estado1)
print(estado2)
print(brasil)
print(brasil[0]['uf'])'''

estado = {} #dicionario
brasil = [] #lista
for c in range(0, 3):
    estado['uf'] = str(input('Unidade federativa:'))
    estado['sigla'] = str(input('Sigla do estado'))
    brasil.append(estado.copy())
print(brasil)